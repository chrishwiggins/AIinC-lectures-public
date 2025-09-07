# SHRDLU Block World Emulator

A Python implementation of Terry Winograd's famous SHRDLU natural language understanding system that can manipulate blocks in a virtual 3D world.

## Overview

SHRDLU was a groundbreaking AI program developed at MIT in the 1960s-70s that demonstrated natural language understanding by allowing users to converse about and manipulate objects in a "blocks world" environment. This emulator recreates the core functionality with:

- **3D Block World**: Virtual environment with colored blocks, pyramids, and boxes
- **Natural Language Processing**: Understanding of commands in plain English
- **Spatial Reasoning**: Physics-based stacking and movement validation
- **Interactive Interface**: Command-line conversation system

## Quick Start

```bash
# Run a demo conversation
make

# Start interactive session
make interactive

# See all available commands
make help
```

## Block World

The virtual world contains various objects with these properties:

**Colors**: red, green, blue, yellow, white, black  
**Shapes**: block, pyramid, box, cube  
**Sizes**: small, medium, large, big, little

### Initial World State
```
Position (1,1): large white box
Position (2,2): large red block -> small blue pyramid
Position (3,2): small green block
Position (5,5): medium yellow block
Position (7,3): small green pyramid
```

## Commands

### Basic Commands
- `show` / `display` / `what` - Show current world state
- `help` / `?` - Show available commands
- `quit` / `exit` / `bye` - Exit the program

### Manipulation Commands
- `pick up <description>` - Pick up a block
  - Example: `pick up the red block`
- `put <block> on <target>` - Place one block on another
  - Example: `put the small pyramid on the large box`

### Query Commands
- `find <description>` - Find blocks matching criteria
  - Example: `find small red blocks`
- `where <description>` - Locate specific blocks
  - Example: `where is the blue pyramid`

### Example Conversations

**Simple Interaction:**
```
SHRDLU> show
Current world state:
==================================================
Position (1,1): large white box
Position (2,2): large red block -> small blue pyramid
...

SHRDLU> find red blocks
The large red block is at position (2,2)

SHRDLU> put the small blue pyramid on the large white box
OK, I put the small blue pyramid on the large white box.
```

**Complex Manipulation:**
```
SHRDLU> put the small green block on the large white box
OK, I put the small green block on the large white box.

SHRDLU> put the small blue pyramid on the small green block  
OK, I put the small blue pyramid on the small green block.

SHRDLU> show
Current world state:
==================================================
Position (1,1): large white box -> small green block -> small blue pyramid
...
```

## Physics Rules

- Blocks stack vertically based on placement order
- Cannot place objects on top of pyramids (they're pointed!)
- Cannot pick up blocks that have something stacked on top
- Larger objects cannot be placed on smaller pyramids
- Gravity automatically restacks remaining blocks when one is moved

## Running Examples

### Make Commands
```bash
make demo        # Quick demo conversation
make quick       # Quick test conversation  
make fun         # Fun pyramid stacking example
make interactive # Interactive session
make basic       # Basic interaction examples
make advanced    # Advanced manipulation examples
make queries     # Search and query examples
make test        # Run all example scripts
```

### Direct Python Execution
```bash
# Interactive session
python3 shrdlu.py

# Run example scripts
python3 example_basic.py
python3 example_advanced.py
python3 example_queries.py
python3 test_comprehensive.py
```

## Files

- `shrdlu.py` - Main SHRDLU emulator
- `example_basic.py` - Basic interaction examples
- `example_advanced.py` - Advanced manipulation scenarios
- `example_queries.py` - Search and query demonstrations
- `test_comprehensive.py` - Complete functionality test
- `Makefile` - Convenient build targets

## Error Handling

The system gracefully handles various error conditions:

- **Ambiguous commands**: Asks for clarification when multiple objects match
- **Impossible operations**: Explains why an action cannot be performed
- **Missing objects**: Reports when requested objects cannot be found
- **Physics violations**: Prevents invalid stacking arrangements

## Implementation Details

Built with Python 3 using:
- Object-oriented design with Block and BlockWorld classes
- Natural language processing with regex-based parsing
- 3D coordinate system for spatial reasoning
- Command-line interface with interactive loop

## Historical Context

The original SHRDLU (1968-1970) was revolutionary for demonstrating that computers could:
- Understand natural language in context
- Reason about physical relationships
- Learn from dialogue and maintain conversation state
- Handle ambiguity through clarifying questions

This implementation captures those core capabilities in a modern, accessible format.

## License

This is an educational recreation of the historical SHRDLU system for learning and demonstration purposes.