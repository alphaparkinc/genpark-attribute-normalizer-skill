from typing import Dict, Any

class AttributeNormalizerClient:
    def normalize(self, attribute_name: str, raw_value: str) -> Dict[str, Any]:
        val = raw_value.strip().lower()
        normalized = raw_value
        if attribute_name == "size":
            size_map = {
                "extra large": "XL", "x-large": "XL", "xl": "XL",
                "large": "L", "medium": "M", "small": "S", "extra small": "XS"
            }
            normalized = size_map.get(val, raw_value)
        elif attribute_name == "color":
            color_map = {
                "dark black": "Black", "slate black": "Black", "pure white": "White", "navy": "Blue"
            }
            normalized = color_map.get(val, raw_value.capitalize())
        return {"normalized_value": normalized}
