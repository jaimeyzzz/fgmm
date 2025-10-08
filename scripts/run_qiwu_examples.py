#!/usr/bin/env python3
"""
Qiwu Examples Runner

A cross-platform script to run Qiwu simulation examples.
This script replaces the Windows batch file for better cross-platform compatibility.
"""

import os
import sys
import glob
import subprocess
from pathlib import Path


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_executable_path():
    """Get the path to the qiwu-example executable."""
    project_root = get_project_root()
    
    # Try different build configurations
    possible_paths = [
        project_root / "build" / "bin" / "Release" / "qiwu-example.exe",  # Windows Release
        project_root / "build" / "bin" / "RelWithDebInfo" / "qiwu-example.exe",  # Windows RelWithDebInfo
        project_root / "build" / "bin" / "qiwu-example",  # Linux/macOS
        project_root / "build" / "qiwu-example",  # Alternative path
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    return None


def get_yaml_configs():
    """Get all available YAML configuration files."""
    project_root = get_project_root()
    yaml_dir = project_root / "resources" / "exps"
    
    if not yaml_dir.exists():
        return []
    
    # Find all YAML files recursively
    yaml_files = []
    for pattern in ["*.yaml", "*.yml"]:
        yaml_files.extend(yaml_dir.rglob(pattern))
    
    # Convert to relative paths from resources directory
    configs = []
    for yaml_file in sorted(yaml_files):
        # Get path relative to resources directory (not project root)
        rel_path = yaml_file.relative_to(project_root / "resources")
        configs.append({
            'path': rel_path,
            'name': yaml_file.stem,
            'full_path': yaml_file
        })
    
    return configs


def display_configs(configs):
    """Display available configuration files."""
    print("\nAvailable configuration files:")
    print("-" * 50)
    
    for i, config in enumerate(configs, 1):
        print(f"{i}. {config['name']}")
    
    print("-" * 50)


def get_user_choice(configs):
    """Get user's choice of configuration file."""
    while True:
        try:
            choice = input(f"Please select configuration file (1-{len(configs)}) or enter 'q' to quit: ").strip()
            
            if choice.lower() == 'q':
                print("Program exit")
                sys.exit(0)
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(configs):
                return configs[choice_num - 1]
            else:
                print(f"Please enter a number between 1 and {len(configs)}")
        except ValueError:
            print("Please enter a valid number or 'q' to quit")


def run_experiment(executable_path, config):
    """Run the selected experiment."""
    project_root = get_project_root()
    
    print(f"\nRunning: {config['name']}")
    print(f"Using executable: {executable_path}")
    print(f"Configuration file: {config['path']}")
    print("-" * 50)
    
    # Change to project root directory
    os.chdir(project_root)
    print(f"Current directory: {os.getcwd()}")
    
    # Prepare command
    cmd = [str(executable_path), str(config['path'])]
    print(f"Executing: {' '.join(cmd)}")
    
    try:
        # Run the experiment
        result = subprocess.run(cmd, check=True)
        print("\nExperiment completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nExperiment failed with return code: {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"\nError: Could not find executable at {executable_path}")
        return False


def main():
    """Main function."""
    print("Qiwu Examples Runner")
    print("=" * 50)
    
    # Check if executable exists
    executable_path = get_executable_path()
    if not executable_path:
        print("Error: Executable not found")
        print("Please make sure the project is compiled")
        print("Expected locations:")
        print("  - build/bin/Release/qiwu-example.exe (Windows)")
        print("  - build/bin/RelWithDebInfo/qiwu-example.exe (Windows)")
        print("  - build/bin/qiwu-example (Linux/macOS)")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check if YAML directory exists
    yaml_dir = get_project_root() / "resources" / "exps"
    if not yaml_dir.exists():
        print(f"Error: YAML config directory not found: {yaml_dir}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Get available configurations
    configs = get_yaml_configs()
    if not configs:
        print("No YAML configuration files found")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Display configurations and get user choice
    display_configs(configs)
    selected_config = get_user_choice(configs)
    
    # Run the experiment
    success = run_experiment(executable_path, selected_config)
    
    # Wait for user input before exiting
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
