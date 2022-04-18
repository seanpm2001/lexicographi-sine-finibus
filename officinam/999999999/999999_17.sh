#!/bin/bash
#===============================================================================
#
#          FILE:  999999_17.sh
#
#         USAGE:  ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD=1 ./999999999/999999_17.sh
#                 FORCE_CHANGED=1 ./999999999/999999_17.sh
#                 FORCE_REDOWNLOAD_REM="1603_1_51" ./999999999/999999_17.sh
#                 time ./999999999/999999_17.sh
#   DESCRIPTION:  ---
#
#       OPTIONS:  ---
#
#  REQUIREMENTS:  - hxltmcli
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Emerson Rocha <rocha[at]ieee.org>
#       COMPANY:  EticaAI
#       LICENSE:  Public Domain dedication
#                 SPDX-License-Identifier: Unlicense
#       VERSION:  v1.0
#       CREATED:  2022-01-13 16:43 UTC started. based on 1603_17_0.sh
#      REVISION:  ---
#===============================================================================
set -e

# time HTTPS_PROXY="socks5://127.0.0.1:9050" ./999999999/999999_17.sh

# ./999999999/0/1603_1.py --codex-de 1603_45_31 --codex-in-tabulam-json | jq
# ./999999999/0/1603_1.py --codex-de 1603_45_31 --codex-in-tabulam-json > 1603/45/31/1603_45_31.mul-Latn.tab.json
# https://commons.wikimedia.org/wiki/Data:Sandbox/EmericusPetro/Example.tab

# @TODO: implement download entire sheet
DATA_1603="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/export?format=xlsx"

# humanitarium_responsum_rem="https://proxy.hxlstandard.org/data/download/humanitarium-responsum-rem_hxl.csv?dest=data_edit&filter01=select&filter-label01=%23status%3E-1&select-query01-01=%23status%3E-1&filter02=cut&filter-label02=HXLated&cut-skip-untagged02=on&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4%2Fedit%23gid%3D1331879749"
DATA_1603_1_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2095477004"
DATA_1603_1_6="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1417450794"
DATA_1603_1_7="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1792999005"
DATA_1603_1_51="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=272891124"
DATA_1603_1_99="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=304729260"
# DATA_1603_17_17="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
# DATA_1603_3_12_6="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1281616178"
# DATA_1603_23_21="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1939636120"
# DATA_1603_23_36="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2020660171"
# DATA_1603_25_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=966182339"
DATA_1603_44_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1333477190"
DATA_1603_44_86="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=447110259"
DATA_1603_44_101="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1448713891"
DATA_1603_44_111="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=2086282985"
DATA_1603_44_142="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=455141043"
DATA_1603_45_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1894917893"
# DATA_1603_45_19="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1703298088"
DATA_1603_45_31="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1610303107"
# DATA_1603_45_95="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1391701984"
# DATA_1603_994_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
# DATA_1603_84_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1366500643"
# DATA_1603_44_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1333477190"
# DATA_1603_44_142="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=455141043"
# DATA_1603_1_51="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=272891124"
# DATA_1603_1_101="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1902379960"
# DATA_1603_63_1="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=80558354"
DATA_1603_63_101="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1462297555"
# DATA_1603_64_604="https://docs.google.com/spreadsheets/d/1ih3ouvx_n8W5ntNcYBqoyZ2NRMdaA0LRg5F9mGriZm4/edit#gid=1016692458"

ROOTDIR="$(pwd)"

# PREFIX_1613_3="1613:3"
# PREFIX_1603_994_1="1603:994:1"
# PREFIX_1603_44_1="1603:44:1"
# PREFIX_1603_44_142="1603:44:142"

# shellcheck source=999999999.lib.sh
. "$ROOTDIR"/999999999/999999999.lib.sh

### Really boostrapping downloads, start _______________________________________
file_download_if_necessary "$DATA_1603_1_1" "1603_1_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_1" "1" "0"

file_download_if_necessary "$DATA_1603_1_99" "1603_1_99" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_99" "1" "0"

# file_download_if_necessary "$DATA_1603_1_6" "1603_1_6" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_6" "1" "0"

file_download_if_necessary "$DATA_1603_1_7" "1603_1_7" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_7" "1" "0"

file_download_if_necessary "$DATA_1603_1_51" "1603_1_51" "csv" "tm.hxl.csv" "hxltmcli" "1"
file_convert_numerordinatio_de_hxltm "1603_1_51" "1" "0"
### Really boostrapping downloads, end _________________________________________

# # FORCE_REDOWNLOAD_REM="1603_1_51"
# file_download_if_necessary "$DATA_1603_1_51" "1603_1_51" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_51" "1" "0"
# # # file_merge_numerordinatio_de_wiki_q "1603_1_51" "0" "0"
# neo_codex_de_numerordinatio "1603_1_51" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_1_51" "0" "0"

# exit 
# file_download_if_necessary "$DATA_1603_45_1" "1603_45_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_45_1" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_45_1" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_45_1" "0" "0"
# file_convert_tmx_de_numerordinatio11 "1603_45_1"
# file_convert_tbx_de_numerordinatio11 "1603_45_1"
# neo_codex_de_numerordinatio "1603_45_1" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_45_1" "0" "0"

# file_download_if_necessary "$DATA_1603_45_1" "1603_45_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# actiones_completis_publicis "1603_45_1"
# upload_cdn "1603_45_1"

# file_download_1603_xlsx "0"
# file_convert_csv_de_downloaded_xlsx "1603_45_1"

# @TODO create a loop on all items from 1603_1_1 with ix_n1603op with flats to
#       allow automation. Then do it.

# temp_save_status "1603_45_1"
# temp_save_status "1603_63_101"
# temp_save_status "1603_45_31"

# file_download_if_necessary "$DATA_1603_1_7" "1603_1_7" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_1_7" "1" "0"
# # file_merge_numerordinatio_de_wiki_q "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_1_7" "0" "0"

# file_download_if_necessary "$DATA_1603_45_31" "1603_45_31" "csv" "tm.hxl.csv" "hxltmcli" "1"
# actiones_completis_publicis "1603_45_31"

# file_download_if_necessary "$DATA_1603_23_21" "1603_23_21" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_23_21" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_23_21" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_23_21" "0" "0"
# file_convert_xml_de_numerordinatio11 "1603_23_21"
# file_convert_tmx_de_numerordinatio11 "1603_23_21"
# file_convert_tbx_de_numerordinatio11 "1603_23_21"
# neo_codex_de_numerordinatio "1603_23_21" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_23_21" "0" "0"

# file_download_if_necessary "$DATA_1603_45_31" "1603_45_31" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_45_31" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_45_31" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_45_31" "0" "0"
# file_convert_xml_de_numerordinatio11 "1603_45_31"
# file_convert_tmx_de_numerordinatio11 "1603_45_31"
# file_convert_tbx_de_numerordinatio11 "1603_45_31"
# neo_codex_de_numerordinatio "1603_45_31" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_45_31" "0" "0"

# upload_cdn "1603_45_31"

# temp_save_status "1603_45_31"

# FORCE_REDOWNLOAD=1 file_download_if_necessary "$DATA_1603_1_1" "1603_1_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# quaero__ix_n1603ia__victionarium_q "1603_1_101" && echo "1603_1_101"
# quaero__ix_n1603ia__victionarium_q "1603_1_101" || echo "1603_1_101"
# quaero__ix_n1603ia__victionarium_q "1603_1_51" && echo "1603_1_51"
# quaero__ix_n1603ia__victionarium_q "1603_45_31" && echo "1603_45_31"
# quaero__ix_n1603ia__victionarium_q "1603_99_987" && echo "1603_99_987"
# actiones_completis_publicis "1603_45_31"
# actiones_completis_publicis "1603_63_101"
file_download_1603_xlsx "0"
# opus_temporibus_cdn
# deploy_0_9_markdown

# quaero__ix_n1603ia__victionarium_q "1603_63_101" && echo "1603_63_101"
# quaero__ix_n1603ia__victionarium_q "1603_1_1" && echo "1603_1_1"

# file_download_if_necessary "$DATA_1603_23_36" "1603_23_36" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_23_36" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_23_36" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_23_36" "0" "0"
# neo_codex_de_numerordinatio "1603_23_36" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_23_36" "0" "0"

# file_download_if_necessary "$DATA_1603_63_1" "1603_63_1" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_63_1" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_63_1" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_63_1" "0" "0"
# neo_codex_de_numerordinatio "1603_63_1" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_63_1" "0" "0"

# file_download_if_necessary "$DATA_1603_45_19" "1603_45_19" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_45_19" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_45_19" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_45_19" "0" "0"
# neo_codex_de_numerordinatio "1603_45_19" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_45_19" "0" "0"

# file_download_if_necessary "$DATA_1603_63_101" "1603_63_101" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_63_101" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_63_101" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_63_101" "0" "0"
# file_convert_tmx_de_numerordinatio11 "1603_63_101"
# file_convert_tbx_de_numerordinatio11 "1603_63_101"
# neo_codex_copertae_de_numerordinatio "1603_63_101" "0" "0"
# neo_codex_de_numerordinatio "1603_63_101" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_63_101" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_63_101" "0" "0"

# upload_cdn "1603_63_101"

# file_download_if_necessary "$DATA_1603_64_41" "1603_64_41" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_64_41" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_64_41" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_64_41" "0" "0"
# neo_codex_de_numerordinatio "1603_64_41" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_64_41" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_64_41" "0" "0"

# file_download_if_necessary "$DATA_1603_44_86" "1603_44_86" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_44_86" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_44_86" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_44_86" "0" "0"
# file_convert_tmx_de_numerordinatio11 "1603_44_86"
# file_convert_tbx_de_numerordinatio11 "1603_44_86"
# neo_codex_copertae_de_numerordinatio "1603_44_86" "0" "0"
# neo_codex_de_numerordinatio "1603_44_86" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_44_86" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_44_86" "0" "0"

# file_download_if_necessary "$DATA_1603_44_101" "1603_44_101" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_44_101" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_44_101" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_44_101" "0" "0"
# file_convert_tmx_de_numerordinatio11 "1603_44_101"
# file_convert_tbx_de_numerordinatio11 "1603_44_101"
# neo_codex_copertae_de_numerordinatio "1603_44_101" "0" "0"
# neo_codex_de_numerordinatio "1603_44_101" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_44_101" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_44_101" "0" "0"

# file_download_if_necessary "$DATA_1603_44_111" "1603_44_111" "csv" "tm.hxl.csv" "hxltmcli" "1"
# file_convert_numerordinatio_de_hxltm "1603_44_111" "1" "0"
# file_translate_csv_de_numerordinatio_q "1603_44_111" "0" "0"
# file_merge_numerordinatio_de_wiki_q "1603_44_111" "0" "0"
# file_convert_tmx_de_numerordinatio11 "1603_44_111"
# file_convert_tbx_de_numerordinatio11 "1603_44_111"
# neo_codex_copertae_de_numerordinatio "1603_44_111" "0" "0"
# neo_codex_de_numerordinatio "1603_44_111" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_44_111" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_44_111" "0" "0"

# neo_codex_de_numerordinatio "1603_1_6" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_1_6" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_1_6" "0" "0"

# neo_codex_de_numerordinatio "1603_1_7" "0" "0"
# neo_codex_copertae_de_numerordinatio "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio_pdf "1603_1_7" "0" "0"
# neo_codex_de_numerordinatio_epub "1603_1_7" "0" "0"

# hxltmcli --objectivum-TMX 1603/1/7/1603_1_7.no1.tm.hxl.csv 1603/1/7/1603_1_7.tmx
# hxltmcli --objectivum-TBX-Basim 1603/1/7/1603_1_7.no1.tm.hxl.csv 1603/1/7/1603_1_7.tbx
#
# hxltmcli --objectivum-TBX-Basim 1603/45/1/1603_45_1.no11.tm.hxl.csv 1603/45/1/1603_45_1.tbx
