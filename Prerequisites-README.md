# Azure AI Agents Labs - Prerequisites and Setup Guide

This document provides a comprehensive checklist of all prerequisites, permissions, and setup steps required to successfully complete the Azure AI Agents Labs.

## Quick Setup Checklist

Use this checklist to track your progress:

- [ ] Azure Subscription with appropriate permissions
- [ ] Azure AI Foundry Resource and Project created
- [ ] Azure AI Search service created and configured
- [ ] Azure OpenAI service created with embedding model
- [ ] Storage Account created
- [ ] Bing Search service created
- [ ] All required permissions assigned
- [ ] Development environment configured
- [ ] Azure CLI authentication completed
- [ ] Lab environment tested

## Detailed Prerequisites Table

| **Component** | **Permission/Resource** | **Summary of Steps** | **Why Required** | **Detailed Steps Reference** | **✓ Done** |
|---------------|------------------------|---------------------|------------------|------------------------------|------------|
| **Azure Subscription** | Contributor or Owner role | Ensure you have sufficient permissions to create resources | Required to create and manage Azure resources | Contact your Azure administrator | [ ] |
| **Azure AI Foundry Resource** | AI Foundry resource creation | Create Azure AI Foundry resource and project | Main platform for AI agent development | Lab 1, Step 1 | [ ] |
| **Azure AI Search Service** | Search service creation | Create Azure AI Search service with Standard tier | Vector database for RAG functionality | Lab 1, Step 2 | [ ] |
| **Azure AI Search - API Access** | Configure API access control | Set API access control to 'Both' | Enable proper authentication methods | Lab 1, Step 2, Point 3 | [ ] |
| **Azure AI Search - Managed Identity** | Enable system-assigned identity | Turn on system-assigned managed identity | Enable secure authentication to other services | Lab 1, Step 2, Point 4 | [ ] |
| **GPT-4o Model Deployment** | Model deployment in AI Foundry | Deploy gpt-4o model with specific settings | Chat completion model for AI agents | Lab 1, Step 3 | [ ] |
| **Azure OpenAI Service** | Separate OpenAI service creation | Create standalone Azure OpenAI service | Required for embedding model (current limitation) | Lab 1, Step 4 | [ ] |
| **Text Embedding Model** | Deploy text-embedding-3-large | Deploy embedding model in Azure OpenAI service | Convert documents to vectors for search | Lab 1, Step 4, Point 6 | [ ] |
| **Storage Account** | Storage account creation | Create storage account for document storage | Store health plan documents for indexing | Lab 1, Step 5 | [ ] |
| **Bing Search Service** | Bing Search resource creation | Create Grounding with Bing Search service | Enhanced search capabilities (Lab 5) | Lab 1, Step 6 | [ ] |

## Required Permissions and Role Assignments

| **Permission** | **From** | **To** | **Role** | **Why Required** | **Detailed Steps** | **✓ Done** |
|----------------|----------|--------|----------|------------------|-------------------|------------|
| **Storage Access** | Search Service Identity | Storage Account | Storage Blob Data Reader | Allow AI Search to read documents from blob storage | Lab 1, Step 7, Point 1 | [ ] |
| **Search Access** | Project Managed Identity | AI Search Resource | Search Index Data Reader | Allow project to read search indices | Lab 1, Step 7, Point 2a | [ ] |
| **Search Management** | Project Managed Identity | AI Search Resource | Search Service Contributor | Allow project to manage search service | Lab 1, Step 7, Point 2b | [ ] |
| **OpenAI Access** | Search Service Identity | Azure OpenAI Resource | Cognitive Services OpenAI User | Allow AI Search to use OpenAI for embeddings | Lab 1, Step 7, Point 3 | [ ] |

## Development Environment Setup

| **Component** | **Action Required** | **Commands/Steps** | **Why Required** | **✓ Done** |
|---------------|--------------------|--------------------|------------------|------------|
| **Python Environment** | Create virtual environment | `python -m venv venv` | Isolate project dependencies | [ ] |
| **Activate Environment** | Activate virtual environment | `venv/Scripts/activate` (Windows) | Use correct Python environment | [ ] |
| **Install Dependencies** | Install required packages | `pip install -r requirements.txt` | Install all required Python libraries | [ ] |
| **Environment Variables** | Create .env file | `cp sample.env .env` | Store configuration securely | [ ] |
| **Configure .env** | Update environment variables | Update AIPROJECT_ENDPOINT, API_KEY, etc. | Connect to your Azure resources | [ ] |
| **Azure CLI Login** | Authenticate with Azure | `az login` | Enable token-based authentication | [ ] |

## Configuration Details

### Environment Variables to Configure

Update your `.env` file with the following values:

| **Variable** | **Source** | **Location in Azure Portal** |
|--------------|------------|------------------------------|
| `AIPROJECT_ENDPOINT` | AI Foundry Project | Project Overview page |
| `API_KEY` | AI Foundry Project | Project Overview page |
| `CHAT_MODEL` | GPT-4o deployment name | Models + endpoints section |
| `CHAT_MODEL_ENDPOINT` | GPT-4o endpoint | Models + endpoints section |

### Resource Naming Conventions

For consistency across labs, use these naming patterns:

- **Resource Group**: `rg-ai-agents-[region]`
- **AI Foundry Project**: `ai-foundry-[your-name]`
- **AI Search Service**: `search-[your-name]`
- **Azure OpenAI**: `openai-[your-name]`
- **Storage Account**: `storage[yourname][random]` (lowercase, no hyphens)

## Validation Steps

### Test Your Setup

After completing all prerequisites, validate your setup:

1. **Run Lab 1, Step 8** - Test environment with joke generation
2. **Verify all resources exist** in your resource group
3. **Check all permissions** are correctly assigned
4. **Ensure .env file** is properly configured

### Common Issues and Solutions

| **Issue** | **Cause** | **Solution** |
|-----------|-----------|--------------|
| Permission denied errors | Missing role assignments | Complete all permissions in Lab 1, Step 7 |
| Authentication failures | Azure CLI not logged in | Run `az login` |
| Model not found errors | Incorrect .env configuration | Verify model names and endpoints |
| Import/vectorize failures | Missing OpenAI permissions | Assign Cognitive Services OpenAI User role |

## Support and Troubleshooting

### Before Starting Labs

- [ ] All checkboxes in this document are marked as complete
- [ ] Test environment passes Lab 1, Step 8 validation
- [ ] All resources are in the same Azure region
- [ ] All resources are in the same resource group

### Getting Help

1. **Review error messages** carefully - they often indicate missing permissions
2. **Check Azure Portal** - verify resources exist and are properly configured
3. **Validate permissions** - ensure all role assignments are complete
4. **Test authentication** - confirm Azure CLI login is active

## Lab-Specific Requirements

### Lab 4 - RAG Agent
- Azure AI Search index with health plan documents
- Connected resources configured in AI Foundry project
- Proper vectorization permissions

### Lab 5 - Multi-Agent System
- All Lab 4 requirements
- Bing Search service for enhanced capabilities

---

## Quick Reference Links

- [Azure AI Foundry Portal](https://ai.azure.com)
- [Azure Portal](https://portal.azure.com)
- [Lab 1 - Complete Setup](./Lab%201%20-%20Project%20Setup.ipynb)
- [Lab 4 - RAG Agent](./Lab%204%20-%20Create%20A%20RAG%20Agent.ipynb)

---

**Note**: This setup is required only once. Once complete, you can proceed through all labs without additional Azure resource creation.
