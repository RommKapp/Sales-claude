#!/usr/bin/env python3
"""
Sales Agent MVP - Optimized version
Simple launch: python main_optimized.py
"""

import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

# LangChain imports
from langchain.schema import HumanMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

# Only OpenAI 
from openai import OpenAI

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SalesAgentOptimized:
    """Optimized call preparation system"""
    
    def __init__(self):
        """System initialization"""
        load_dotenv()
        
        # Check API keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        # Initialize OpenAI and LangChain
        self.openai_client = OpenAI(api_key=self.openai_api_key)
        
        # LangChain with memory for context between stages
        self.llm = ChatOpenAI(
            api_key=self.openai_api_key,
            model="gpt-4",  # Use standard model for LangChain
            temperature=0.1
        )
        self.memory = ConversationBufferMemory(return_messages=True)
        
        # Setup paths
        self.setup_directories()
        
        # Analysis context
        self.conversation_context = ""
        self.company_data = None
        self.products_data = None
    
    def setup_directories(self):
        """Create necessary directories"""
        self.input_dir = Path("input_data")
        self.output_dir = Path("output_data")
        self.prompts_dir = Path("prompts")
        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"Configured directories: {self.input_dir}, {self.output_dir}, {self.prompts_dir}")
    
    def read_file(self, filepath):
        """Read file with error handling"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            logger.info(f"Read file: {filepath}")
            return content
        except Exception as e:
            logger.error(f"Error reading file {filepath}: {e}")
            return None
    
    def write_file(self, filepath, content):
        """Write file with error handling"""
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            logger.info(f"Written file: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error writing file {filepath}: {e}")
            return False
    
    def call_o3_with_web_search(self, input_text, max_retries=3):
        """
        Call OpenAI O3 with real web search
        """
        for attempt in range(max_retries):
            try:
                logger.info(f"Calling O3 API with web search (attempt {attempt + 1}/{max_retries})")
                
                # Check that we're using real web search
                resp = self.openai_client.responses.create(
                    model="o3",
                    input=input_text,
                    tools=[{"type": "web_search"}],  # Real web search
                    # include=["web_search_call.results"]  # Can include for debugging
                )
                
                result = resp.output_text
                logger.info(f"Received response from O3: {len(result)} characters")
                
                # Check that web search was actually used
                if "http" in result or "www." in result or "based on" in result.lower():
                    logger.info("✅ Web search working - found links in response")
                else:
                    logger.warning("⚠️ Web search might not be used - no links in response")
                
                return result
                
            except Exception as e:
                logger.error(f"Error calling O3 API (attempt {attempt + 1}): {e}")
                if attempt == max_retries - 1:
                    raise
        
        return None

    def call_o3_with_code_interpreter(self, input_text, max_retries=3):
        """
        Call OpenAI O3 with Code Interpreter for calculations
        """
        for attempt in range(max_retries):
            try:
                logger.info(f"Calling O3 API with Code Interpreter (attempt {attempt + 1}/{max_retries})")
                
                # Use Code Interpreter for calculations
                resp = self.openai_client.responses.create(
                    model="o3",
                    input=input_text,
                    instructions="When solving math or analyzing metrics, write and run Python code first. Always use code interpreter for calculations.",
                    tools=[{
                        "type": "code_interpreter",
                        "container": {"type": "auto"}
                    }],
                    stream=False
                )
                
                result = resp.output
                logger.info(f"Received response from O3 with calculations: {len(str(result))} characters")
                
                # Check that code was actually executed
                result_text = str(result)
                if "code_interpreter_call" in result_text or "import" in result_text or "=" in result_text:
                    logger.info("✅ Code Interpreter working - found signs of code execution")
                else:
                    logger.warning("⚠️ Code Interpreter might not have been used")
                
                # Extract text response from response
                if hasattr(result, 'output_text'):
                    return result.output_text
                elif isinstance(result, list):
                    # Look for text response in list elements
                    for item in result:
                        if hasattr(item, 'content') and isinstance(item.content, list):
                            for content_item in item.content:
                                if hasattr(content_item, 'text'):
                                    return content_item.text
                        elif hasattr(item, 'text'):
                            return item.text
                
                return str(result)
                
            except Exception as e:
                logger.error(f"Error calling O3 API with Code Interpreter (attempt {attempt + 1}): {e}")
                if attempt == max_retries - 1:
                    # Fallback to regular web search if Code Interpreter unavailable
                    logger.warning("Code Interpreter unavailable, using regular web search")
                    return self.call_o3_with_web_search(input_text, max_retries)
        
        return None
    
    def step0_load_data(self):
        """Step 0: Load input data"""
        logger.info("=== Step 0: Load input data ===")
        
        # Read data
        company_file = self.input_dir / "company_description.txt"
        self.company_data = self.read_file(company_file)
        
        products_file = self.input_dir / "avaliable_products.txt"
        self.products_data = self.read_file(products_file)
        
        if not self.company_data or not self.products_data:
            raise ValueError("Failed to load input data")
        
        # Initialize context for LangChain
        self.conversation_context = f"""# Context for company analysis

## Company description:
{self.company_data}

## Available products:
{self.products_data}

## Analysis date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        
        # Add to LangChain memory
        self.memory.chat_memory.add_user_message(self.conversation_context)
        
        # Create Step 0 file
        step0_content = f"""# Step 0 - Initial Data Load
{self.conversation_context}

## Status
✅ Data loaded and passed to LangChain memory
- Company description: {len(self.company_data)} characters
- Available products: {len(self.products_data)} characters
"""
        
        output_file = self.output_dir / "step0_initial_data.txt"
        self.write_file(output_file, step0_content)
        
        logger.info("Step 0 completed - data loaded into LangChain")
        return True
    
    def execute_step(self, step_number, step_name, prompt_filename, output_filename):
        """Universal function for executing Steps 1-8"""
        logger.info(f"=== Step {step_number}: {step_name} ===")
        
        # Read prompt
        prompt_file = self.prompts_dir / prompt_filename
        prompt_template = self.read_file(prompt_file)
        
        if not prompt_template:
            logger.error(f"CRITICAL ERROR: Failed to read prompt {prompt_filename}")
            return False
        
        logger.info(f"✅ Prompt loaded: {len(prompt_template)} characters")
        
        # Get conversation history from LangChain
        messages = self.memory.chat_memory.messages
        history_context = "\n".join([f"**{type(msg).__name__}**: {msg.content}" for msg in messages[-5:]])  # Last 5 messages
        
        # Create full prompt with context
        full_prompt = f"""# Context from previous analysis stages:
{history_context}

# Task for Step {step_number}:
{prompt_template}

IMPORTANT: Use context from previous stages to create coherent analysis. Must use web search to get current company information.
"""
        
        logger.info(f"Context passed: {len(history_context)} characters from LangChain")
        
        try:
            # Determine if Code Interpreter needed for calculations
            calculation_steps = [3, 4, 7]  # Steps requiring calculations
            
            if step_number in calculation_steps:
                logger.info(f"📊 Step {step_number} requires calculations - using Code Interpreter")
                # Add instruction for calculations
                calculation_prompt = f"""{full_prompt}

IMPORTANT: This stage requires precise calculations and mathematical analysis. 
Must use Python code for all calculations:
- Financial metrics (revenue per employee, cost calculations)
- Percentage ratios and ROI
- Performance analysis and baseline indicators
- Potential savings and payback calculations

Show all calculations using code for analysis transparency."""
                
                result = self.call_o3_with_code_interpreter(calculation_prompt)
            else:
                # Regular steps with web search
                result = self.call_o3_with_web_search(full_prompt)
            
            if result:
                # Add result to LangChain memory
                self.memory.chat_memory.add_ai_message(f"Step {step_number} result: {result}")
                
                # Save file
                output_file = self.output_dir / output_filename
                final_content = f"# Step {step_number} - {step_name}\n\n{result}"
                
                if self.write_file(output_file, final_content):
                    logger.info(f"✅ Step {step_number} completed successfully")
                    return True
            
        except Exception as e:
            logger.error(f"❌ Error in Step {step_number}: {e}")
        
        return False
    
    def run_full_analysis(self):
        """Run full analysis Steps 0-8"""
        logger.info("🚀 Starting full Sales Agent MVP analysis")
        
        # Define all stages
        steps = [
            (0, "Initial Data Load", None, None, self.step0_load_data),
            (1, "Company Snapshot", "Step1-Prompt-snapshot.md", "step1_company_snapshot.txt"),
            (2, "Tech Stack Analysis", "Step2-Prompt-tech-stack.md", "step2_tech_stack.txt"),
            (3, "Performance Baseline", "Step3-Prompt-performance-baselines.md", "step3_performance_baseline.txt"),
            (4, "Business Plan", "Step4-Prompt-quantified-business-plan.md", "step4_business_plan.txt"),
            (5, "Stakeholders", "Step5-Stakeholders-buying-process.md", "step5_stakeholders.txt"),
            (6, "Product Mapping", "Step6-Product-Solution-Mapping.md", "step6_product_mapping.txt"),
            (7, "Value Map", "Step7-Prompt-value-map.md", "step7_value_map.txt"),
            (8, "Call Script", "Step8-Prompt-how-to-write-1st-call.md", "step8_call_script.txt"),
        ]
        
        success_count = 0
        
        for step_data in steps:
            step_num = step_data[0]
            step_name = step_data[1]
            
            try:
                if step_num == 0:
                    # Step 0 uses special function
                    success = step_data[4]()
                else:
                    # Steps 1-8 use universal function
                    prompt_file = step_data[2]
                    output_file = step_data[3]
                    success = self.execute_step(step_num, step_name, prompt_file, output_file)
                
                if success:
                    success_count += 1
                    logger.info(f"✅ Step {step_num} ({step_name}) - SUCCESS")
                else:
                    logger.error(f"❌ Step {step_num} ({step_name}) - ERROR")
                    
            except Exception as e:
                logger.error(f"❌ Step {step_num} ({step_name}) - CRITICAL ERROR: {e}")
        
        # Final report
        logger.info(f"📊 Analysis completed: {success_count}/{len(steps)} stages successful")
        
        if success_count == len(steps):
            print(f"\n🎉 All stages completed successfully!")
            print(f"📁 Results: {self.output_dir}/")
            print(f"📞 Final script: {self.output_dir}/step8_call_script.txt")
            
            # Check LangChain memory size
            memory_size = len(str(self.memory.chat_memory.messages))
            logger.info(f"📝 LangChain memory: {memory_size} characters of context")
            
            return True
        else:
            print(f"\n⚠️ Completed {success_count} out of {len(steps)} stages")
            return False

def main():
    """Main function - simple launch of full analysis"""
    try:
        print("🚀 Sales Agent MVP - Starting analysis")
        print("="*50)
        
        # Create system
        agent = SalesAgentOptimized()
        
        # Run full analysis
        success = agent.run_full_analysis()
        
        if success:
            print("\n" + "="*50)
            print("🎉 ANALYSIS COMPLETED SUCCESSFULLY!")
            print("📞 First call script ready")
        else:
            print("\n" + "="*50)
            print("⚠️ Analysis completed with errors")
            
    except Exception as e:
        logger.error(f"💥 Critical error: {e}")
        print(f"\n💥 Error: {e}")

if __name__ == "__main__":
    main()