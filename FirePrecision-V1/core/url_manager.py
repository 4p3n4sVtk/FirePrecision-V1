import json
import random
from pathlib import Path

class URLManager:
    def __init__(self):
        self.config_path = Path(__file__).parent.parent / "config" / "url_config.json"
        self.load_config()
        
    def load_config(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except:
            self.config = {
                "domains": {
                    "ifood": "oferta.ifood.com.br",
                    "shopee": "promo.shopee.com.br",
                    "aliexpress": "desconto.aliexpress.com"
                },
                "path_templates": {
                    "ifood": ["cupom/{id}", "desconto/{id}", "promo/{id}"],
                    "shopee": ["flash-sale/{id}", "super-oferta/{id}"],
                    "aliexpress": ["deal/{id}", "special/{id}"]
                }
            }
            self.save_config()
    
    def save_config(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4)
    
    def generate_pretty_url(self, service_name, real_url):
        if service_name not in self.config["domains"]:
            return {
                "display": real_url,
                "real": real_url,
                "type": "direct"
            }
        
        url_id = ''.join(random.choices('abcdefghjkmnpqrstuvwxyz23456789', k=8))
        path_template = random.choice(self.config["path_templates"][service_name])
        path = path_template.format(id=url_id)
        
        return {
            "display": f"https://{self.config['domains'][service_name]}/{path}",
            "real": real_url,
            "type": "masked"
        }