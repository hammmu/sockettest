import asyncio
import websockets
import time
async def send_image(websocket, path):
    print("im here in request")
    try:
        for i in range(0, 4):
            with open("test" + str(i + 1) + ".png", "rb") as image_file:
                chunk_size = 524288  # Adjust the chunk size as needed
                while True:
                    image_chunk = image_file.read(chunk_size)

                    if not image_chunk:
                        print("im here")
                        break  # End of file

                    # Send the image chunk
                    await websocket.send(image_chunk)
                await websocket.send("done")

    except websockets.ConnectionClosed:
        print("Connection closed by the client")

start_server = websockets.serve(send_image, "0.0.0.0", 80)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
