# test_mcp.py
import asyncio
from agents.mcp.server import MCPServerStdio


async def test_mcp():
    yfinance_server = MCPServerStdio(
        params={
            "command": "uvx",
            "args": ["mcp-yahoo-finance"],
        },
        cache_tools_list=True,
    )

    try:
        async with yfinance_server:
            print("✅ MCP 서버 연결 성공!")
            # 사용 가능한 도구 목록 확인
            tools = await yfinance_server.list_tools()
            print(f"사용 가능한 도구: {tools}")
    except Exception as e:
        print(f"❌ 에러 발생: {e}")


if __name__ == "__main__":
    asyncio.run(test_mcp())