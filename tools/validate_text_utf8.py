#!/usr/bin/env python3
"""Fail closed on invalid UTF-8 and high-confidence mojibake in tracked text."""
from __future__ import annotations
import argparse,pathlib,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
TEXT_SUFFIXES={'.md','.txt','.tex','.bib','.json','.yml','.yaml','.py','.toml','.cff','.csv'}
MARKERS=tuple(bytes.fromhex(value).decode('utf-8') for value in ('c383c692','c383c2a2','c3a2e282ac','c3a2e282acc284','c3afc2bfc2bd','efbfbd'))
def tracked_files():
 raw=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT)
 return [ROOT/pathlib.Path(item.decode()) for item in raw.split(b'\0') if item]
def validate(paths):
 failures=[]
 for path in paths:
  if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {'LICENSE'}:continue
  try:text=path.read_text(encoding='utf-8')
  except UnicodeDecodeError as error:failures.append({'path':str(path.relative_to(ROOT)),'reason':f'invalid UTF-8: {error}' });continue
  found=sorted(marker for marker in MARKERS if marker in text)
  if found:failures.append({'path':str(path.relative_to(ROOT)),'reason':'high-confidence mojibake markers: '+','.join(found)})
 return failures
def main(argv=None):
 parser=argparse.ArgumentParser();parser.add_argument('paths',nargs='*');args=parser.parse_args(argv)
 paths=[ROOT/pathlib.Path(item) for item in args.paths] if args.paths else tracked_files();failures=validate(paths)
 for item in failures:print(f"{item['path']}: {item['reason']}",file=sys.stderr)
 if failures:return 1
 print(f'UTF-8 text validation passed: {len(paths)} tracked/requested files checked.')
 return 0
if __name__=='__main__':raise SystemExit(main())
