# Performance Comparison: Python 3.13 vs Python 3.13t (No GIL)

## Overview
This project benchmarks the execution time of a CPU-bound task (finding prime numbers) using three different approaches:
- **Single-threaded execution**
- **Multi-threaded execution** (concurrent execution with Python threads)
- **Multi-processing execution** (parallel execution using multiple processes)

The goal is to compare the performance of Python **3.13** (with GIL) and Python **3.13t** (without GIL) to analyze the impact of disabling the Global Interpreter Lock (GIL) on multi-threading.

## Prerequisites
- Install **Python 3.13** (standard version)
```sh
  uv python install 3.13
  ```
- Install **Python 3.13t** (experimental version with GIL disabled) 
```sh
  uv python install 3.13t
  ```
- Init the project usig uv:
  ```sh
  uv init
  ```
  *(No external dependencies required, as only built-in modules are used)*

## Running the Benchmark
Run the script using both Python versions:

### Python 3.13 (with GIL)
```sh
uv run --python 3.13 .\compare_execution_time.py
```

### Python 3.13t (without GIL)
```sh
uv run --python 3.13t .\compare_execution_time.py
```

## Expected Results
- **Python 3.13:** Multi-threading should not significantly improve performance due to the GIL.
- **Python 3.13t:** Multi-threading should show notable speedup since the GIL is disabled, allowing true parallel execution on multi-core CPUs.
- **Multi-processing:** Should perform similarly in both versions, as it is not affected by the GIL.

## Notes
- The benchmark uses a **CPU-bound task** (prime number counting) to highlight GIL limitations in Python 3.13.
- Performance may vary depending on system hardware (e.g., number of CPU cores).

## Conclusion
This project demonstrates the impact of the **GIL** on Python's execution model. The results will help determine whether disabling the GIL in **Python 3.13t** provides real performance benefits for CPU-bound multi-threaded applications.

