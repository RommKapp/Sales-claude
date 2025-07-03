# Sales Agent MVP - First Call Preparation System

Automated company analysis and script generation system for salespeople, using **only OpenAI O3 + built-in web search** and **LangChain** for context passing.

## 🎯 What the system does

Analyzes companies in 8 steps and creates a ready-to-use script for the first call:

1. **Step 0** - Load input data into LangChain memory
2. **Step 1** - Company Snapshot (with real web search)
3. **Step 2** - Tech Stack Analysis 
4. **Step 3** - Performance Baseline Analysis
5. **Step 4** - Business Plan Analysis
6. **Step 5** - Stakeholders Analysis
7. **Step 6** - Product Solution Mapping
8. **Step 7** - Value Map Analysis
9. **Step 8** - Call Script Generation

## 🚀 Simple Launch

### 1. Install dependencies
```bash
# Activate virtual environment
source sales-agent-env/bin/activate

# Install packages (Tavily removed)
pip install -r requirements.txt
```

### 2. Setup API keys
Add only OpenAI key to `.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Prepare data
The system uses ready-made files:
- `input_data/company_description.txt` - client company description
- `input_data/avaliable_products.txt` - available products

### 4. Launch (just one command!)
```bash
python main.py
```

## 📁 Project Structure

```
Sales-claude/
├── main.py                    # Main script
├── requirements.txt           # Dependencies
├── .env                      # API keys
├── input_data/               # Input data
│   ├── company_description.txt
│   └── avaliable_products.txt
├── output_data/              # Analysis results
│   ├── step0_initial_data.txt
│   ├── step1_company_snapshot.txt
│   ├── step2_tech_stack.txt
│   ├── step3_performance_baseline.txt
│   ├── step4_business_plan.txt
│   ├── step5_stakeholders.txt
│   ├── step6_product_mapping.txt
│   ├── step7_value_map.txt
│   └── step8_call_script.txt
└── prompts/                  # Prompts for each stage
    ├── Step1-Prompt-snapshot.md
    ├── Step2-Prompt-tech-stack.md
    └── ...
```

## ⚡ Technical Details

- **Model**: OpenAI O3 with real web search (not emulator!)
- **LangChain**: Full context transfer between stages
- **Execution time**: ~1-2 minutes per stage  
- **Error handling**: 3 attempts for each API call
- **Logging**: Detailed logs + web search verification
- **Optimization**: Single main.py file for all stages

## 🎉 Result

After execution, 8 files will appear in `output_data/` with detailed analysis and ready-to-use call script.

---

**Status**: ✅ Ready working MVP system