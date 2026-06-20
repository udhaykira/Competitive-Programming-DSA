"""
Problem : Stock Span Problem

For each day's stock price, find the **span**, i.e., the number of consecutive days (including today) for which the price was **less than or equal to today's price.

"""

def calculate_stock_spans(prices: list[int]) -> list[int]:
    spans = []
    stack = []
    
    for price in prices:
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]
            
        stack.append((price, span))
        spans.append(span)
        
    return spans

if __name__ == "__main__":
    input_prices = [100, 80, 60, 70, 60, 75, 85]
    output_spans = calculate_stock_spans(input_prices)
    
    print(f"Input Prices: {input_prices}")
    print(f"Output Spans: {output_spans}")