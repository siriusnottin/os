#!/usr/bin/env python3

import os, subprocess, json
from alive_progress import alive_bar

import logging
STATUS = {
  'success': 'Done',
  'fail': 'Fail'
}

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

from tabulate import tabulate

EXCLUDED_PUBLISHERS = ('Adobe',) # not used for now
DEFAULT_APP_DIR = '/Applications'
APP_INSTALLERS = {
  'Setapp': f'{DEFAULT_APP_DIR}/Setapp'
}

def get_macos_apps(apps_dir='/Applications'):

  apps = []

  excluded_words = (
  '.DS_Store',
  'autoupdate',
  'uninstall',
  'uninstaller'
  )

  logging.debug(f'get_macos_apps called with {apps_dir}')
  apps_count=0
  not_app_count = 0
  ignored_words_count = 0
  for app in os.listdir(apps_dir):
    logging.debug(f'Checking {app}...')
    apps_count+=1
    if any(word.lower() in app.lower() for word in excluded_words):
      logging.debug(f'{app} contains an ignored word, skipping...')
      ignored_words_count+=1
      continue
    if not '.app' in app:
      logging.debug(f'{app} is not an app, skipping...')
      not_app_count+=1
      continue
    apps.append({
      'name': app.replace('.app', ''),
      'installation_method': 'N/A'
    })
  logging.info(f'Found {apps_count} apps in {apps_dir} [%s]' % STATUS['success'])
  table = [[apps_count, not_app_count, ignored_words_count]]
  headers = ['Found', 'Not App', 'Ignored Words']
  print(tabulate(table, headers, tablefmt='github'))

  return apps

def get_macos_apps_installer(installers=APP_INSTALLERS):
  apps = []
  for installer in installers:
    logging.info(f'Getting apps installed by {installer}... [%s]' % STATUS['success'])
    for app_dir in os.listdir(APP_INSTALLERS[installer]):
      get_macos_apps(app_dir)

def get_app_publisher(app_path):
  try:
    result = subprocess.run(['mdls', '-name', 'kMDItemCFBundleIdentifier', app_path], capture_output=True, text=True)
    logging.info(f'Getting publisher for {app_path}... [%s]' % STATUS['success'])
    if result.returncode == 0:
      return result.stdout
  except Exception as e:
    logging.error(f'Error getting publisher for {app_path}... [%s]' % STATUS['fail'])
  return 'Unknown'
    
def display_apps(apps):
  table = [[app['name'], 'N/A', app['installation_method']] for app in apps]
  headers = ['App Name', 'Publisher', 'Installation Method']
  print(tabulate(table, headers, tablefmt='github', showindex='always'))
    
json_file_name = 'mac_apps.json'
json_file_path = os.path.join(os.getcwd(), json_file_name)
def create_json_file(data, file_path=json_file_path):
  with open(file_path, 'w') as f:
    f.write(json.dumps(data))
  logging.info(f'Exprting applications list to {json_file_path}... [%s]' % STATUS['success'])

if __name__ == '__main__':
  with alive_bar(spinner='classic', bar=None) as bar:
    mac_apps = get_macos_apps('/Applications')
    create_json_file({'MacOS Applications': mac_apps})
    # create a json file, and add mac_apps to it
    # get_macos_apps_installer(APP_INSTALLERS)
    bar()
