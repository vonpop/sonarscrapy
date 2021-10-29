import scrapy
import json
    
class ProjectsSpider(scrapy.Spider):
    name = 'projects'
    ip_or_domain = '<insert your sonarqube IP/domain>'
    allowed_domains = [ip_or_domain]
    start_urls = [f'http://{ip_or_domain}:9000/api/components/search?qualifiers=TRK']
    http_user = '<insert your sonarqube access token>'
    http_pass = ''

    def parse(self, response):
        json_response = json.loads(response.text)
        components = json_response["components"]
        yield components
        for component in components:
            project_key = component["key"] 
			# to discover which metrics exist
			# use the endpoint api/metrics/search 
            metric_keys = "blocker_violations,bugs,classes,code_smells,cognitive_complexity,comment_lines,comment_lines_density,comment_lines_data,class_complexity,file_complexity,function_complexity,complexity_in_classes,complexity_in_functions,branch_coverage,coverage,complexity,last_commit_date,duplicated_blocks,duplicated_files,duplicated_lines,file_complexity_distribution,files,function_complexity_distribution,line_coverage,lines,ncloc,ncloc_language_distribution,reliability_rating,security_hotspots,security_rating,statements,vulnerabilities"
            measures_url = f'http://{ProjectsSpider.ip_or_domain}:9000/api/measures/component?component={project_key}&metricKeys={metric_keys}'
            yield response.follow(measures_url, callback=self.parse_measures)

    def parse_measures(self, response):
        json_response = json.loads(response.text)
        component = json_response["component"]
        measures = component["measures"]
        for measure in measures:
            yield {"component": component["key"], "metric": measure["metric"], "value": measure["value"]}
        