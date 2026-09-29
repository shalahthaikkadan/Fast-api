from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = []


# Product data
class Product(BaseModel):
    name: str
    price: float
    quantity: int


# Add product
@app.post("/addproduct")
def add_product(product: Product):

    if product.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )

    if product.quantity < 1 or product.quantity > 100:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be between 1 and 100"
        )

    products.append(product)

    return {
        "message": "Product added successfully",
        "product": product
    }


# Get all products
@app.get("/getproducts")
def get_products():

    return {
        "products": products
    }


# Update product
@app.put("/updateproduct/{index}")
def update_product(index: int, product: Product):

    if index < 0 or index >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )

    if product.quantity < 1 or product.quantity > 100:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be between 1 and 100"
        )

    products[index] = product

    return {
        "message": "Product updated successfully",
        "product": product
    }


# Delete product
@app.delete("/deleteproduct/{index}")
def delete_product(index: int):

    if index < 0 or index >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    deleted_product = products.pop(index)

    return {
        "message": "Product deleted successfully",
        "product": deleted_product
    }


# Get one product
@app.get("/getproduct/{index}")
def get_product(index: int):

    if index < 0 or index >= len(products):
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return products[index]


# Calculate total
@app.get("/total")
def get_total():

    total = 0

    for product in products:
        total = total + (product.price * product.quantity)

    return {
        "total": total
    }


# JSON format for adding a product:
#
# {
#     "name": "Wireless Mouse",
#     "price": 799,
#     "quantity": 2
# }