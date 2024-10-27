"""Constants for the Extended OpenAI Conversation integration."""

DOMAIN = "extended_openai_conversation"
DEFAULT_NAME = "Extended OpenAI Conversation"
CONF_ORGANIZATION = "organization"
CONF_BASE_URL = "base_url"
DEFAULT_CONF_BASE_URL = "https://api.openai.com/v1"
CONF_API_VERSION = "api_version"
CONF_SKIP_AUTHENTICATION = "skip_authentication"
DEFAULT_SKIP_AUTHENTICATION = False

EVENT_AUTOMATION_REGISTERED = "automation_registered_via_extended_openai_conversation"
EVENT_CONVERSATION_FINISHED = "extended_openai_conversation.conversation.finished"

CONF_PROMPT = "prompt"
DEFAULT_PROMPT = """I want you to act as smart home manager of Home Assistant.
I will provide information of smart home and Food Menu along with a question, you will truthfully make correction or answer using information provided in minimal sentence in everyday language.

Below is Lunch Food Menu
MONDAY
Grilled Cheese & Ham SandwichServed with tomato soup
Raspberry Mousse with Chocolate

TUESDAY
Boneless Chicken BitesServed with fresh vegetables and dip
Homemade Empire Cookie

WEDNESDAY
B.L.T.Served on whole wheat toast with onion rings
Fresh Fruit Bowl

THURSDAY
Deluxe PizzaTopped with pepperoni, mushrooms and bell peppers, served
with tossed salad
Chocolate Dipped Pineapple and Whipped Cream

FRIDAY
Dublin Coddle- Irish sausage, bacon, onion and potato hotpot, served with a
warm dinner roll
Butterscotch Ripple Ice Cream

SATURDAY
Blueberry PancakesServed with maple syrup and breakfast sausage
Mandarin Orange Jello

SUNDAY
Bacon & Scrambled EggsServed with toast and sliced oranges
Banana Bread
ALTERNATE LUNCH CHOICE:  SOUP or SALAD & SANDWICH
TURKEY & HAVARTI/EGG SALAD / CHICKEN SALAD
ALTERNATE DESSERT - FRUIT SALAD OR COOKIES

Below is Dinner Food Menu
MONDAY
Turkey SchnitzelBreaded turkey topped with cranberry sauce, served with
mixed vegetables and mashed potatoes
Apple Strudel

TUESDAY
Fettucine and Chicken AlfredoServed with toasted garlic bread and Caesar
salad
Chocolate Eclair

WEDNESDAY
Butter ChickenServed with mashed yams and peas
Walnut Bread Pudding

THURSDAY
Chinese  DinnerSweet  and  sour  chicken  balls,  egg  roll  and vegetable  fried
rice
Lemon Mousse and Fortune Cookie

FRIDAY
Pork SouvlakiSkewered and marinated pork served with tzatziki sauce,
pita bread and steamed broccoli
Cinnamon Bun

SATURDAY
Beef Stir FryServed on noodles
Vanilla Strawberry Parfait

SUNDAY
Braised BBQ Pork RibsServed with baked potatoes & steamed vegetables
Red Velvet Cake
ALTERNATE SUPPER CHOICESBEEF POT PIE, CHICKEN or SALMON

Current Time: {{now()}}.
"""
CONF_CHAT_MODEL = "chat_model"
DEFAULT_CHAT_MODEL = "gpt-3.5-turbo-1106"
CONF_MAX_TOKENS = "max_tokens"
DEFAULT_MAX_TOKENS = 150
CONF_TOP_P = "top_p"
DEFAULT_TOP_P = 1
CONF_TEMPERATURE = "temperature"
DEFAULT_TEMPERATURE = 0.5
CONF_MAX_FUNCTION_CALLS_PER_CONVERSATION = "max_function_calls_per_conversation"
DEFAULT_MAX_FUNCTION_CALLS_PER_CONVERSATION = 1
CONF_FUNCTIONS = "functions"
DEFAULT_CONF_FUNCTIONS = [
    {
        "spec": {
            "name": "execute_services",
            "description": "Use this function to execute service of devices in Home Assistant.",
            "parameters": {
                "type": "object",
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "domain": {
                                    "type": "string",
                                    "description": "The domain of the service",
                                },
                                "service": {
                                    "type": "string",
                                    "description": "The service to be called",
                                },
                                "service_data": {
                                    "type": "object",
                                    "description": "The service data object to indicate what to control.",
                                    "properties": {
                                        "entity_id": {
                                            "type": "string",
                                            "description": "The entity_id retrieved from available devices. It must start with domain, followed by dot character.",
                                        }
                                    },
                                    "required": ["entity_id"],
                                },
                            },
                            "required": ["domain", "service", "service_data"],
                        },
                    }
                },
            },
        },
        "function": {"type": "native", "name": "execute_service"},
    }
]
CONF_ATTACH_USERNAME = "attach_username"
DEFAULT_ATTACH_USERNAME = False
CONF_USE_TOOLS = "use_tools"
DEFAULT_USE_TOOLS = False
CONF_CONTEXT_THRESHOLD = "context_threshold"
DEFAULT_CONTEXT_THRESHOLD = 13000
CONTEXT_TRUNCATE_STRATEGIES = [{"key": "clear", "label": "Clear All Messages"}]
CONF_CONTEXT_TRUNCATE_STRATEGY = "context_truncate_strategy"
DEFAULT_CONTEXT_TRUNCATE_STRATEGY = CONTEXT_TRUNCATE_STRATEGIES[0]["key"]

SERVICE_QUERY_IMAGE = "query_image"

CONF_PAYLOAD_TEMPLATE = "payload_template"
