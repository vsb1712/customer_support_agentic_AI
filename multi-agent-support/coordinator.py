from agents import faq_agent, order_agent, ticket_agent, response_agent

def process_query(query):

    result = faq_agent.handle(query)
    if result:
        return response_agent.format_response(result)

    result = order_agent.handle(query)
    if result:
        return response_agent.format_response(result)

    result = ticket_agent.handle(query)
    return response_agent.format_response(result)
