class Scraper():
    def __init__(self, json_data):
        self.json_data = json_data

    def get_data(self):
        export_data = []

        for field in self.json_data:
            data_sample = {}
            data_sample['id'] = field['id']
            data_sample['date'] = field['created_at']
            data_sample['text'] = field['text']
            data_sample['likes'] = field['favorite_count']
            data_sample['retweets'] = field['retweet_count']
            export_data.append(data_sample)
        
        return export_data
