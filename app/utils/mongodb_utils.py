from app.db.mongodb_database import get_mongo_connection

# Alternative version if you have a timestamp field
def get_user_history(limit=12):
    """
    Extract latest conversations where user_type="assistant" using timestamp.
    """
    try:
        collection = get_mongo_connection()
        
        # Query for user_type="assistant" and sort by timestamp (descending)
        assistant_conversations = list(
            collection.find(
                {"user_type": "user"}
            )
            .sort("timestamp", -1)  # Sort by timestamp descending (latest first)
            .limit(limit)
        )
        
        print(f"Found {len(assistant_conversations)} assistant conversations")
        return assistant_conversations
        
    except Exception as e:
        print(f"Error fetching assistant conversations: {e}")
        return []



