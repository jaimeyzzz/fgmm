# FGMM 

Code for SIGGRAPH Asia 2025 paper - Fast Galerkin Multigrid Method for Unstructured Meshes

## Quick Start

### Prerequisites

- C++20 compatible compiler (GCC 10+, Clang 12+, MSVC 2019+)
- CUDA Toolkit (optional, for GPU acceleration)
- CMake 3.16+
- Python 3.6+ (for Python bindings)

### Building

```bash
# Clone the repository
git clone git@github.com:jaimeyzzz/fgmm.git
cd fgmm

# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ..

# Build
make -j$(nproc)  # Linux/macOS
# or
cmake --build . --config Release  # Windows
```

### Running Examples

```bash
# Run examples using the Python script
python scripts/run_qiwu_examples.py
```

## Project Structure

```
fgmm/
├── external/qiwu/          # Core simulation library
│   ├── qiwu/               # Main source code
│   │   ├── core/           # C++ computational kernels
│   │   ├── python/         # Python bindings
│   │   ├── examples/       # Example applications
│   │   └── tests/          # Test suite
│   └── external/           # Third-party dependencies
├── resources/              # Configuration files and scenes
├── scripts/                # Build and utility scripts
└── output/                 # Simulation results
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built on top of the Qiwu physics simulation framework