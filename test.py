from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res = tavily_search("Best hotels in Paris")
# print(res)

flight_info = search_flights("Plan a trip from Nepal to Bangladesh next month")
print(flight_info)