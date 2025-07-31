#!/usr/bin/env python3
import os
import argparse
from tqdm import tqdm

def write_chunk(part, lines, header, base_name):
    filename = f"{base_name}_part_{part}.csv"
    with open(filename, 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)
    print(f"✅ Created chunk {part}: {filename} ({len(lines)} lines)")

def split_csv_by_size(input_file, chunk_size_bytes):
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    total_size = os.path.getsize(input_file)
    print(f"📁 Splitting '{input_file}' (~{total_size // (1024 * 1024)} MB) into ~{chunk_size_bytes // (1024 * 1024)} MB chunks...")

    with open(input_file, 'r') as f:
        header = f.readline()
        lines = []
        part = 1
        current_size = len(header.encode('utf-8'))
        progress = tqdm(total=total_size, unit='B', unit_scale=True, desc="Progress")

        for line in f:
            line_size = len(line.encode('utf-8'))
            current_size += line_size
            lines.append(line)
            progress.update(line_size)

            if current_size >= chunk_size_bytes:
                write_chunk(part, lines, header, base_name)
                part += 1
                lines = []
                current_size = len(header.encode('utf-8'))

        if lines:
            write_chunk(part, lines, header, base_name)

        progress.close()
        print(f"🏁 Splitting complete. {part} file(s) generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file into smaller chunks")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("--chunk_size_mb", type=int, default=500, help="Chunk size in megabytes")
    args = parser.parse_args()

    chunk_size_bytes = args.chunk_size_mb * 1024 * 1024
    split_csv_by_size(args.input_file, chunk_size_bytes)
