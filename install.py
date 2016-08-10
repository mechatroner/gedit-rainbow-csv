#!/usr/bin/env python

'''Gedit Rainbow csv installation script.
  1. copies lang files to ~/.local/share/gtksourceview-3.0/language-specs
  2. copies plugin files to ~/.local/share/gedit/plugins
  3. copies existing styles xml files to ~/.local/share/gtksourceview-3.0/styles
  4. patches style files (old files would be backed up in ~/.local/share/styles_backup)
'''

import sys
import os
import argparse
import shutil

#TODO ensure gedit version >= 3 before installation. error otherwise


script_dir = os.path.dirname(os.path.realpath(__file__))
langs_path = ['.local', 'share', 'gtksourceview-3.0', 'language-specs']
styles_path = ['.local', 'share', 'gtksourceview-3.0', 'styles']
plugin_path = ['.local', 'share', 'gedit', 'plugins']
backup_path = ['.local', 'share', 'styles_backup']


def copy_dir_content(src_dir, dst_dir):
    src_files = os.listdir(src_dir)
    for file_name in src_files:
        full_file_name = os.path.join(src_dir, file_name)
        if (os.path.isfile(full_file_name)):
            dst_path = os.path.join(dst_dir, file_name)
            if not os.path.exists(dst_path):
                shutil.copyfile(full_file_name, dst_path)


def ensure_path(components):
    cur_dir = os.path.expanduser('~')
    for c in components:
        cur_dir = os.path.join(cur_dir, c)
        if not os.path.exists(cur_dir):
            os.mkdir(cur_dir)
    return cur_dir


patch_content = '''
  <!-- Rainbow csv -->
  <style name="csv:srbcol1"             foreground="#FF0000" bold="true"/>
  <style name="csv:srbcol2"             foreground="#0000FF" bold="true"/>
  <style name="csv:srbcol3"             foreground="#00A000" bold="true"/>
  <style name="csv:srbcol4"             foreground="#FF00FF" bold="true"/>
  <style name="csv:srbcol5"             foreground="#964B00" bold="true"/>
  <style name="csv:srbcol6"             foreground="#FF0000" bold="false"/>
  <style name="csv:srbcol7"             foreground="#0000FF" bold="false"/>
  <style name="csv:srbcol8"             foreground="#009000" bold="false"/>
  <style name="csv:srbcol9"             foreground="#FF00FF" bold="false"/>
'''


def patch_hacky(src_path, dst_path):
    found_style = False
    content = open(src_path, 'r').readlines()
    for line in content:
        if line.startswith('</style-scheme>'):
            found_style = True
        if line.find('<style name="csv:') != -1:
            return False
    if not found_style:
        return False
    with open(dst_path, 'w') as dst:
        for line in content:
            if line.startswith('</style-scheme>'):
                result = True
                dst.write(patch_content)
            dst.write(line)
    return True


def patch_styles():
    styles_dir = ensure_path(styles_path)
    source_dir = '/usr/share/gtksourceview-3.0/styles'
    copy_dir_content(source_dir, styles_dir)
    backup_dir = ensure_path(backup_path)
    style_files = os.listdir(styles_dir)
    style_files = [f for f in style_files if f.endswith('.xml')]
    patched_any = False
    for f in style_files:
        fp = os.path.join(styles_dir, f)
        ftmp = os.path.join(backup_dir, '{}.new'.format(f))
        success = patch_hacky(fp, ftmp)
        patched_any = patched_any or success
        if success:
            shutil.copyfile(fp, os.path.join(backup_dir, f))
            os.rename(ftmp, fp)
    if patched_any:
        print 'Done. Old style files are saved here:', backup_dir


def copy_lang_files():
    langs_dir = ensure_path(langs_path)
    for f in ['csv.lang', 'tsv.lang']:
        shutil.copyfile(os.path.join(script_dir, f), os.path.join(langs_dir, f))


def copy_plugin_files():
    plugin_dir = ensure_path(plugin_path)
    for f in ['rainbow_csv.plugin', 'rainbow_csv.py']:
        shutil.copyfile(os.path.join(script_dir, f), os.path.join(plugin_dir, f))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--patch_style_xmls', action='store_true', help='patch style xmls only')
    args = parser.parse_args()
    if args.patch_style_xmls:
        patch_styles()
        return
    copy_lang_files()
    copy_plugin_files()
    patch_styles()


if __name__ == '__main__':
    main()
