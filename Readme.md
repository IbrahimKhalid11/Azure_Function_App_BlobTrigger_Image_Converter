# Azure Blob Storage Image Converter

## **📌 Overview**
This Azure Function automatically converts any uploaded image to **PNG format** and resizes it before saving it to a separate Blob Storage container.

- **Trigger:** Blob Storage (New file uploaded to `raw/` container)
- **Output:** Converted and resized image stored in `processed/` container
- **Supported Formats:** JPG, JPEG, BMP, GIF, TIFF, etc.

---

## **🚀 How It Works**
1. **Upload an image** to the `raw/` Blob Storage container.
2. The Azure Function automatically:
   - Reads the uploaded image.
   - Converts it to PNG format.
   - Resizes it to a predefined size (e.g., 512x512).
   - Saves the processed image to the `processed/` container.
3. The converted file is accessible in Azure Storage.

---

## **📂 Project Structure**
Azure Blob Image Converter  
```
│-- function_app.py        # Azure Function logic  
│-- requirements.txt       # Dependencies for the function  
│-- host.json              # Azure Function host configuration  
│-- .funcignore            # Files to ignore in deployment  
│-- .gitignore             # Git ignored files  
│-- README.md              # Project documentation  
│-- local.settings.json    # Local Azure function settings  
├── .vscode/               # VS Code workspace settings  
│   ├── extensions.json    
│   ├── launch.json    
│   ├── settings.json    
│   ├── tasks.json    
├── raw/                   # Input container (Trigger Source) in Azure
└── processed/             # Output container in Azure
 ```


---

## **🔧 Installation & Setup**
### **1️⃣ Prerequisites**
- **Azure Account** with **Storage Account**
- **Azure Functions Core Tools**
- **Python 3.8+**
- **VS Code** with Azure Extensions

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
