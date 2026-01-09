# Knowledge Graph Constructor with Schema.org

Automatic Knowledge Graph Constructor using LLM-based entity extraction and Schema.org type alignment.

## Overview

This project provides a pipeline for automatically building knowledge graphs from unstructured text. It uses Large Language Models (LLMs) to extract entities and relationships, then aligns them with [Schema.org](https://schema.org/) types and properties to create standards-compliant knowledge graphs.

### Key Features

- **LLM-based Entity Extraction**: Automatically identifies entities (people, organizations, places, events, products) from text
- **Schema.org Alignment**: Maps extracted entities to standard Schema.org types
- **Relationship Extraction**: Discovers relationships between entities using Schema.org properties
- **Multiple Output Formats**: Export as JSON-LD or RDF/Turtle
- **Queryable**: Ask questions about the constructed knowledge graph

### Architecture

```
Text Input
    ↓
[SchemaOrgEntityExtractor]
    ↓ (uses LLM)
Entities + Relations
    ↓
[KnowledgeGraphConstructor]
    ↓
Knowledge Graph
    ↓
JSON-LD / RDF Output
```

**Components:**

1. **schema_loader.py**: Loads and queries Schema.org type definitions
2. **schemaorg_memory_entry.py**: Pydantic models for entities, relations, and graph entries
3. **schemaorg_entity_extractor.py**: LLM-based entity and relation extraction
4. **knowledge_graph_constructor.py**: Main class for building and querying knowledge graphs
5. **config.py**: Configuration settings and constants
6. **example_usage.py**: Example script demonstrating usage

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or compatible LLM endpoint)

### Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `rdflib>=6.0.0` - RDF graph manipulation
- `pydantic>=2.0.0` - Data validation and models
- `openai>=1.0.0` - LLM API client
- `numpy>=1.20.0` - Numerical operations

### Environment Setup

Set your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### Basic Example

```python
from knowledge_graph_constructor import KnowledgeGraphConstructor

# Initialize the constructor
kg = KnowledgeGraphConstructor(
    api_key="your-openai-api-key",
    model="gpt-4"
)

# Add text to extract entities and relations
kg.add_text(
    "Alice works at Google as a software engineer. She met Bob at "
    "TechConference 2025 in San Francisco."
)

# Finalize the knowledge graph
kg.finalize()

# Get statistics
stats = kg.get_stats()
print(f"Entities: {stats['entities']}, Relations: {stats['relations']}")

# Query the knowledge graph
answer = kg.query("Where does Alice work?")
print(answer)

# Export as JSON-LD
jsonld = kg.to_jsonld()

# Export as RDF/Turtle
rdf = kg.to_rdf()
```

### Run the Example Script

```bash
python example_usage.py
```

### Expected Output

The example script will:

1. Extract entities and relations from sample text
2. Print statistics about the knowledge graph
3. Answer a query about the extracted information
4. Export the knowledge graph in JSON-LD and RDF/Turtle formats
5. Save outputs to `output.jsonld` and `output.ttl`

**Sample JSON-LD Output:**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@id": "urn:kg:entity-id-1",
      "@type": "Person",
      "name": "Alice",
      "jobTitle": "software engineer",
      "worksFor": {
        "@id": "urn:kg:entity-id-2"
      }
    },
    {
      "@id": "urn:kg:entity-id-2",
      "@type": "Organization",
      "name": "Google"
    },
    {
      "@id": "urn:kg:entity-id-3",
      "@type": "Person",
      "name": "Bob",
      "jobTitle": "CEO"
    }
  ]
}
```

**Sample RDF/Turtle Output:**

```turtle
@prefix schema: <https://schema.org/> .
@prefix kg: <urn:kg:> .

kg:entity-id-1 a schema:Person ;
    schema:name "Alice" .

kg:entity-id-1 schema:worksFor kg:entity-id-2 .

kg:entity-id-2 a schema:Organization ;
    schema:name "Google" .
```

## Supported Entity Types

The system supports the following Schema.org types:

- **Person**: Individuals
- **Organization**: Companies, institutions, corporations
- **Place**: Locations, cities, countries
- **Event**: Conferences, meetings, gatherings
- **Product**: Products, software applications
- **CreativeWork**: Articles, books, movies

## Supported Relationships

Common Schema.org properties used for relationships:

- `worksFor`: Person employed by Organization
- `location`: Entity located at Place
- `knows`: Person knows Person
- `attendee`: Person attended Event
- `manufacturer`: Organization produces Product
- `founder`: Person founded Organization
- `memberOf`: Person/Organization member of Organization
- `author`: Person authored CreativeWork

## Advanced Usage

### Custom LLM Configuration

```python
# Use a different model
kg = KnowledgeGraphConstructor(
    api_key="your-api-key",
    model="gpt-3.5-turbo"
)

# Use a custom endpoint
kg = KnowledgeGraphConstructor(
    api_key="your-api-key",
    model="custom-model",
    base_url="https://your-custom-endpoint.com/v1"
)
```

### Query the Knowledge Graph

```python
# Ask questions about extracted information
answer = kg.query("Who is the CEO of StartupXYZ?")
answer = kg.query("Where is the conference located?")
answer = kg.query("What does Alice do?")
```

### Multiple Text Inputs

```python
kg.add_text("First piece of information...")
kg.add_text("Second piece of information...")
kg.add_text("Third piece of information...")
kg.finalize()
```

## Project Structure

```
simplemem_schemaorg-kg-constructor/
├── schema_loader.py              # Schema.org type definitions
├── schemaorg_memory_entry.py     # Pydantic models
├── schemaorg_entity_extractor.py # LLM-based extraction
├── knowledge_graph_constructor.py # Main constructor class
├── config.py                      # Configuration settings
├── example_usage.py               # Example script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── LICENSE                        # License information
└── .gitignore                     # Git ignore rules
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See the [LICENSE](LICENSE) file for details.

## References

- [Schema.org](https://schema.org/) - Structured data vocabulary
- [JSON-LD](https://json-ld.org/) - JSON-based linked data format
- [RDF](https://www.w3.org/RDF/) - Resource Description Framework

## Citation

If you use this project in your research, please cite:

```bibtex
@software{schemaorg_kg_constructor,
  title = {Knowledge Graph Constructor with Schema.org},
  author = {SimpleMem Contributors},
  year = {2025},
  url = {https://github.com/imadcat/simplemem_schemaorg-kg-constructor}
}
```
