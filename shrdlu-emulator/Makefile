.PHONY: test demo basic advanced queries comprehensive interactive clean help

# Default target - run a demo conversation
all: demo

# Interactive SHRDLU session
interactive:
	@echo "Starting interactive SHRDLU session..."
	@echo "Type 'help' for commands, 'quit' to exit"
	@echo ""
	python3 shrdlu.py

# Quick demo conversation
demo:
	@echo "=== SHRDLU Demo Conversation ==="
	@echo ""
	@echo "Commands: show -> find red blocks -> put small blue pyramid on large white box -> show"
	@echo ""
	@echo "show\nfind red blocks\nput the small blue pyramid on the large white box\nshow\nquit" | python3 shrdlu.py

# Run basic examples
basic:
	@echo "Running basic interaction examples..."
	python3 example_basic.py

# Run advanced examples  
advanced:
	@echo "Running advanced manipulation examples..."
	python3 example_advanced.py

# Run query examples
queries:
	@echo "Running query and search examples..."
	python3 example_queries.py

# Run comprehensive test suite
comprehensive:
	@echo "Running comprehensive test suite..."
	python3 test_comprehensive.py

# Run all example scripts
test: basic advanced queries comprehensive

# Quick test conversation
quick:
	@echo "=== Quick SHRDLU Test ==="
	@echo ""
	@echo "show\nfind small things\npick up the small green block\nput the small green block on the large white box\nshow\nquit" | python3 shrdlu.py

# Fun conversation example
fun:
	@echo "=== Fun SHRDLU Conversation ==="
	@echo ""
	@echo "show\nfind pyramids\nput the small blue pyramid on the medium yellow block\nput the small green pyramid on the small blue pyramid\nshow\nfind green things\nquit" | python3 shrdlu.py

# Show available targets
help:
	@echo "SHRDLU Makefile Commands:"
	@echo ""
	@echo "  make          - Run demo conversation (default)"
	@echo "  make demo     - Run demo conversation"
	@echo "  make quick    - Run quick test conversation"
	@echo "  make fun      - Run fun example conversation"
	@echo "  make interactive - Start interactive SHRDLU session"
	@echo ""
	@echo "Example Scripts:"
	@echo "  make basic    - Run basic interaction examples"
	@echo "  make advanced - Run advanced manipulation examples"
	@echo "  make queries  - Run query and search examples"
	@echo "  make comprehensive - Run comprehensive test suite"
	@echo "  make test     - Run all example scripts"
	@echo ""
	@echo "  make clean    - Remove any temporary files"
	@echo "  make help     - Show this help message"

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete 2>/dev/null || true
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@echo "Clean complete."