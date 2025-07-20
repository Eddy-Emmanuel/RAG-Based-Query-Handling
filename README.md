# Healthcare Insurance RAG Assessment

**Assessment Submission**: Intelligent Healthcare Insurance Advisory System using RAG (Retrieval-Augmented Generation)

## 🎯 Assessment Overview

This project implements a sophisticated RAG-based system that provides intelligent healthcare insurance advice for FlexiCare, PrimeCare, and ZenCare plans. The solution combines document retrieval with AI-powered question answering to deliver accurate, contextual responses about insurance coverage.

## 🏗️ My Approach

### Architecture Design
I built a multi-layered RAG system that separates concerns between document processing, vector storage, and query handling:

1. **Document Processing Layer**: Uses Google Gemini 2.5 Pro for robust PDF content extraction
2. **Vector Storage Layer**: ChromaDB for efficient similarity-based document retrieval  
3. **Query Processing Layer**: OpenAI GPT-4o-mini for generating structured, domain-specific responses
4. **API Layer**: FastAPI for clean, RESTful endpoints

### Key Technical Decisions

**Multi-Model Strategy**: 
- **Gemini 2.5 Pro** for PDF processing (superior document understanding)
- **GPT-4o-mini** for response generation (cost-effective, fast inference)
- **OpenAI Embeddings** for semantic search (proven performance)

**RAG Implementation**:
- Used LangChain's RetrievalQA chain for seamless retrieval-generation pipeline
- Implemented similarity search with top-k=3 for balanced context vs. noise
- Custom prompt template ensuring healthcare domain expertise and structured outputs

**Data Processing Pipeline**:
```python
PDF → Base64 → Gemini Extraction → Document Chunks → Embeddings → ChromaDB
```

## 🚀 How to Run the Solution

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Google Gemini API Key
- Jupyter Notebook

### Quick Start

1. **Clone the repository**
   ```bash
   git clone [your-repo-link]
   cd healthcare-rag-assessment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your-openai-key
   GEMINI_API_KEY=your-gemini-key
   ```

4. **Process documents (one-time setup)**
   ```bash
   # Place your PDF files in the pdfs/ directory
   # Run the data extraction and preprocessing notebook
   jupyter notebook experiment.ipynb
   ```
   Execute all cells in the notebook to:
   - Extract content from PDF documents using Gemini
   - Create document embeddings
   - Store vectors in ChromaDB

5. **Start the server**
   ```bash
   python main.py
   ```

6. **Test the system**
   ```bash
   curl -X POST "http://localhost:8000/ai/rag/" \
        -H "Content-Type: application/json" \
        -d '{"user_query": "What are the zencare monthly benefits"}'
   ```

### API Documentation
Access interactive docs at: `http://localhost:8000/docs`

## 📊 System Architecture
```mermaid
graph TB
    A[PDF Documents] --> B[Gemini 2.5 Pro]
    B --> C[Document Processing]
    C --> D[Text Chunks]
    D --> E[OpenAI Embeddings]
    E --> F[ChromaDB Vector Store]
    G[User Query] --> H[Retriever]
    F --> H
    H --> I[Retrieved Context]
    I --> J[GPT-4o-mini]
    J --> K[Structured Response]
```

## 🔧 System Components

### Core Files
- `main.py` - FastAPI application and server setup
- `endpoint_router/rag_endpoint.py` - API route handlers
- `utils/rag_utils.py` - RAG chain and document processing utilities
- `experiment.ipynb` - Data extraction, preprocessing, and vector storage notebook
- `.env` - Environment configuration (API keys)
- `env_config/config.py` - Configuration loader

### RAG Chain Configuration
```python
# Retriever settings
search_type="similarity"
search_kwargs={"k": 3}

# LLM settings  
model="gpt-4o-mini"
temperature=0  # Deterministic responses for consistency
```

### Custom Prompt Template
Specialized prompt ensuring:
- Healthcare domain expertise
- Plan-specific accuracy
- Structured markdown responses
- Clear limitation statements
- Actionable guidance

## 📊 Example Usage

**Input Query:**
```json
{
  "question": "What are the key differences between FlexiCare and PrimeCare deductibles?"
}
```

**System Response:**
```markdown
## FlexiCare vs PrimeCare Deductible Comparison

### FlexiCare
- Individual deductible: $1,500
- Family deductible: $3,000
- Out-of-network: $2,500 individual

### PrimeCare  
- Individual deductible: $500
- Family deductible: $1,000
- Out-of-network: $1,500 individual

### Key Takeaway
PrimeCare offers significantly lower deductibles, making it more cost-effective for frequent healthcare users.
```

## 🎯 Assessment Highlights

### Technical Excellence
- **Modular Architecture**: Clean separation of concerns
- **Error Handling**: Robust error management throughout the pipeline
- **Scalability**: Vector store design supports easy document addition
- **Performance**: Optimized retrieval with configurable search parameters

### Domain Expertise
- **Healthcare Focus**: Specialized prompt engineering for insurance domain
- **Accuracy**: Source attribution and limitation transparency
- **Usability**: Structured responses with actionable insights

### Innovation
- **Multi-Model Integration**: Leveraging strengths of different AI models
- **PDF Processing**: Advanced document extraction with Gemini's multimodal capabilities
- **API Design**: RESTful endpoints for easy integration

## 🔍 Testing the Solution

### Sample Questions to Try
1. "What preventive care is covered under ZenCare?"
2. "Compare prescription drug coverage across all three plans"
3. "What are the out-of-network penalties for PrimeCare?"
4. "How do I file a claim for FlexiCare?"

### Expected Behavior
- Responses cite specific plan documents
- Clear statements when information isn't available
- Structured comparisons using tables/lists
- Actionable next steps included

## 📈 Future Enhancements

- Real-time document updates
- Multi-language support  
- Advanced query understanding with intent detection
- Integration with live insurance APIs
- Conversation memory for follow-up questions

## 🛡️ Error Handling

The system gracefully handles:
- Missing API keys with clear error messages
- Document processing failures
- Empty retrieval results
- Malformed queries

## 📝 Assessment Notes

This solution demonstrates:
- **Full-stack RAG implementation** from document processing to API deployment
- **Production-ready code** with proper error handling and configuration management
- **Domain expertise** in healthcare insurance through specialized prompting
- **Scalable architecture** supporting easy extension and maintenance
