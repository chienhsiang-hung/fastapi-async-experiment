import asyncio
import httpx
import time

# 設定要打的目標和併發數量
URL_SYNC = "http://127.0.0.1:8000/sync-endpoint"
URL_ASYNC = "http://127.0.0.1:8000/async-endpoint"
REQUESTS_COUNT = 50

async def fetch(client, url):
    """發送單一請求"""
    response = await client.get(url, timeout=20.0)
    return response.status_code

async def run_test(url, name):
    """同時發出多個請求並計算總時間"""
    print(f"\n🚀 開始測試 [{name}] - 發送 {REQUESTS_COUNT} 個請求...")
    
    start_time = time.time()
    
    # 建立一個非同步的 HTTP 客戶端
    async with httpx.AsyncClient() as client:
        # 準備好 50 個任務
        tasks = [fetch(client, url) for _ in range(REQUESTS_COUNT)]
        # asyncio.gather 會將這 50 個任務同時丟出去
        await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"✅ [{name}] 總耗時: {end_time - start_time:.2f} 秒")

async def main():
    # 先測試 Async
    await run_test(URL_ASYNC, "非同步 (Async)")
    
    # 再測試 Sync
    await run_test(URL_SYNC, "同步 (Sync)")

if __name__ == "__main__":
    asyncio.run(main())