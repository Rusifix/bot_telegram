from pyrogram import Client

api_id = 5800659162
api_hash = "AAGzxmLva6wVFznCC87jDuuyLbZ1Gflmn0U"

with Client('account', api_id, api_hash) as app:
    app.send_message('@Rusifix','Greeting from **Pyrogram**!')