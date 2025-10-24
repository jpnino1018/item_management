from fastapi import FastAPI
import pydantic
app = FastAPI()

# Defines a Pydantic model for an item
class Item(pydantic.BaseModel):
    name: str
    price: float

# In-memory storage for items
items = {}

# Endpoint to list all items
@app.get("/items/", response_model=list[Item])
async def read_items():
    return list(items.values())

# Endpoint to create a new item
@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.name in items:
        raise pydantic.ValidationError(f"Item with name {item.name} already exists.")
    items[item.name] = item
    return item

# Endpoint to get a specific item by name
@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    if item_name not in items:
        raise pydantic.ValidationError(f"Item with name {item_name} not found.")
    return items[item_name]

