import pandas as pd
import os

# Sample product data
products_data = [
    {
        "ProductID": 1,
        "ProductName": "Laptop Pro X1",
        "Category": "Electronics",
        "Price": 1299.99,
        "StockQuantity": 25,
        "SupplierName": "TechCorp Inc",
        "Description": "High-performance laptop with 16GB RAM and 512GB SSD",
        "SKU": "LPX1-001",
        "Weight": "2.1 kg",
        "Dimensions": "35.5 x 24.2 x 1.8 cm"
    },
    {
        "ProductID": 2,
        "ProductName": "Wireless Mouse Elite",
        "Category": "Electronics",
        "Price": 89.99,
        "StockQuantity": 150,
        "SupplierName": "PeripheralTech",
        "Description": "Ergonomic wireless mouse with precision tracking",
        "SKU": "WME-002",
        "Weight": "0.12 kg",
        "Dimensions": "12 x 6.5 x 4 cm"
    },
    {
        "ProductID": 3,
        "ProductName": "Office Chair Premium",
        "Category": "Furniture",
        "Price": 549.99,
        "StockQuantity": 45,
        "SupplierName": "ComfortSeating Ltd",
        "Description": "Ergonomic office chair with lumbar support and adjustable height",
        "SKU": "OCP-003",
        "Weight": "18.5 kg",
        "Dimensions": "68 x 68 x 110-120 cm"
    },
    {
        "ProductID": 4,
        "ProductName": "4K Monitor 27 inch",
        "Category": "Electronics",
        "Price": 399.99,
        "StockQuantity": 32,
        "SupplierName": "DisplayTech Solutions",
        "Description": "27-inch 4K UHD monitor with HDR support",
        "SKU": "4KM27-004",
        "Weight": "6.8 kg",
        "Dimensions": "61.4 x 36.6 x 5.2 cm"
    },
    {
        "ProductID": 5,
        "ProductName": "Standing Desk Converter",
        "Category": "Furniture",
        "Price": 299.99,
        "StockQuantity": 28,
        "SupplierName": "WorkSpace Dynamics",
        "Description": "Adjustable standing desk converter for healthier work posture",
        "SKU": "SDC-005",
        "Weight": "12.3 kg",
        "Dimensions": "80 x 50 x 15-45 cm"
    },
    {
        "ProductID": 6,
        "ProductName": "Mechanical Keyboard RGB",
        "Category": "Electronics",
        "Price": 149.99,
        "StockQuantity": 75,
        "SupplierName": "KeyTech Pro",
        "Description": "Mechanical gaming keyboard with RGB backlighting",
        "SKU": "MKR-006",
        "Weight": "1.1 kg",
        "Dimensions": "44 x 13.5 x 3.5 cm"
    },
    {
        "ProductID": 7,
        "ProductName": "Webcam HD Pro",
        "Category": "Electronics",
        "Price": 129.99,
        "StockQuantity": 60,
        "SupplierName": "VisionTech",
        "Description": "1080p HD webcam with auto-focus and noise cancellation",
        "SKU": "WHP-007",
        "Weight": "0.2 kg",
        "Dimensions": "9.5 x 2.7 x 2.7 cm"
    },
    {
        "ProductID": 8,
        "ProductName": "Desk Lamp LED",
        "Category": "Furniture",
        "Price": 79.99,
        "StockQuantity": 95,
        "SupplierName": "Illumination Co",
        "Description": "Adjustable LED desk lamp with touch controls and USB charging",
        "SKU": "DLL-008",
        "Weight": "1.2 kg",
        "Dimensions": "45 x 20 x 8 cm"
    },
    {
        "ProductID": 9,
        "ProductName": "Bluetooth Headphones",
        "Category": "Electronics",
        "Price": 199.99,
        "StockQuantity": 42,
        "SupplierName": "AudioMax",
        "Description": "Noise-cancelling Bluetooth headphones with 30-hour battery",
        "SKU": "BTH-009",
        "Weight": "0.25 kg",
        "Dimensions": "19 x 17 x 8 cm"
    },
    {
        "ProductID": 10,
        "ProductName": "External Hard Drive 2TB",
        "Category": "Electronics",
        "Price": 89.99,
        "StockQuantity": 120,
        "SupplierName": "StorageTech",
        "Description": "Portable 2TB external hard drive with USB 3.0",
        "SKU": "EHD2TB-010",
        "Weight": "0.3 kg",
        "Dimensions": "11.5 x 8.2 x 1.5 cm"
    },
    {
        "ProductID": 11,
        "ProductName": "Tablet Stand Adjustable",
        "Category": "Furniture",
        "Price": 39.99,
        "StockQuantity": 200,
        "SupplierName": "AccessoryPlus",
        "Description": "Multi-angle adjustable stand for tablets and phones",
        "SKU": "TSA-011",
        "Weight": "0.5 kg",
        "Dimensions": "18 x 12 x 3 cm"
    },
    {
        "ProductID": 12,
        "ProductName": "USB-C Hub 7-in-1",
        "Category": "Electronics",
        "Price": 69.99,
        "StockQuantity": 85,
        "SupplierName": "ConnectTech",
        "Description": "7-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader",
        "SKU": "UCH7-012",
        "Weight": "0.15 kg",
        "Dimensions": "12 x 3.5 x 1.2 cm"
    }
]

# Create DataFrame
df = pd.DataFrame(products_data)

# Create the Excel file
output_file = "Products.xlsx"
df.to_excel(output_file, index=False, sheet_name="Products")

print(f"✅ Created {output_file} with {len(products_data)} products")
print(f"📊 Columns: {list(df.columns)}")
print(f"📁 File saved in: {os.path.abspath(output_file)}")
