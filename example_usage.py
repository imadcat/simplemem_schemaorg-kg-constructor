#!/usr/bin/env python3
"""
Example usage of the Knowledge Graph Constructor.
"""

import json
import os
from knowledge_graph_constructor import KnowledgeGraphConstructor


def main():
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        print("Warning: OPENAI_API_KEY not set. Set it with: export OPENAI_API_KEY='your-key'")
        print("Using placeholder for demonstration...")
        api_key = "your-openai-api-key"
    
    # Initialize the constructor
    print("Initializing Knowledge Graph Constructor...")
    kg = KnowledgeGraphConstructor(
        api_key=api_key,
        model="gpt-4"
    )
    
    # Add text inputs
    print("\nAdding text 1...")
    kg.add_text(
        "Alice works at Google as a software engineer. She met Bob at the "
        "TechConference 2025 in San Francisco. Bob is the CEO of StartupXYZ.",
        timestamp="2025-01-09T10:00:00"
    )
    
    print("Adding text 2...")
    kg.add_text(
        "StartupXYZ is located in Palo Alto and focuses on AI products. "
        "Their flagship product is called SmartBot.",
        timestamp="2025-01-09T11:00:00"
    )
    
    # Finalize
    kg.finalize()
    
    # Print statistics
    stats = kg.get_stats()
    print(f"\nKnowledge Graph Statistics:")
    print(f"  Entities: {stats['entities']}")
    print(f"  Relations: {stats['relations']}")
    print(f"  Texts processed: {stats['texts_processed']}")
    
    # Query
    print("\n--- Query ---")
    question = "Where does Bob's company operate from?"
    print(f"Question: {question}")
    answer = kg.query(question)
    print(f"Answer: {answer}")
    
    # Export as JSON-LD
    print("\n--- JSON-LD Output ---")
    jsonld = kg.to_jsonld()
    print(json.dumps(jsonld, indent=2))
    
    # Export as RDF/Turtle
    print("\n--- RDF/Turtle Output ---")
    rdf = kg.to_rdf()
    print(rdf)
    
    # Save outputs
    with open("output.jsonld", "w") as f:
        json.dump(jsonld, f, indent=2)
    print("\nSaved JSON-LD to output.jsonld")
    
    with open("output.ttl", "w") as f:
        f.write(rdf)
    print("Saved RDF/Turtle to output.ttl")


if __name__ == "__main__":
    main()
