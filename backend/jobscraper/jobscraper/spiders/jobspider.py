import scrapy

from jobscraper.items import JobItem


class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["www.impactpool.org"]
    start_urls = ["https://www.impactpool.org/search"]

    def parse(self, response):
        jobs = response.css('a.apply-link ::attr(href)')

        for job in jobs:
            #job_url = f"www.impactpool.org{job.get()}"
            job_url = job.get()
            yield response.follow(job_url, callback=self.parse_job_page)

        next_page = response.css('div#show_more a.ip-cta::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            self.logger.info('No more pages to parse.')

        

    def parse_job_page(self, response):

        raw_job_description = response.xpath('//div[@class="job-description"]//text()').getall()
        pruned_descripton = [text.strip() for text in raw_job_description if text.strip()]
        filtered_descripton = [element for element in pruned_descripton if element != "\n"]
        clean_job_description = ' '.join(filtered_descripton)

        job_item = JobItem()
        job_item["job_title"] = response.css('section.job-title h1::text').get()
        job_item["organization"] = response.xpath('//span[text()="Organization:"]/following::text()[1]').get().strip()
        job_item["location"] = response.xpath('//span[text()="Location:"]/following::text()[1]').get().strip()
        job_item["grade"] = response.xpath('//span[text()="Grade:"]/following::text()[1]').get().strip().replace("\n", "")
        job_item["occupational_groups"] = response.xpath('//span[text()="Occupational Groups:"]/following-sibling::ul/li/text()').getall()
        job_item["closing_date"] = response.xpath('//span[text()="Closing Date:"]/following::text()[1]').get().strip()
        job_item["job_description"] = clean_job_description

        yield job_item
