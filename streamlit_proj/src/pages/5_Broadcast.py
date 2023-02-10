from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import asyncio
import websockets
from streamlit.components.v1 import html

CONNECTIONS = set()

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def broadcast_messages():
    while True:
        message = "Hello Fundpark"
        websockets.broadcast(CONNECTIONS, message)
        await asyncio.sleep(100)

async def main():
    async with websockets.serve(register, "localhost", 4854):
        await broadcast_messages()

if __name__ == "__main__":
    asyncio.run(main())

js = """
window.addEventListener("DOMContentLoaded", () => {
  const messages = document.createElement("ul");
  document.body.appendChild(messages);

  const websocket = new WebSocket("ws://localhost:4854/");
  websocket.onmessage = ({ data }) => {
    const message = document.createElement("li");
    const content = document.createTextNode(data);
    message.appendChild(content);
    messages.appendChild(message);
  };
});
"""
html = f"<script>{js}</script>"
