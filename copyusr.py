from pymongo import MongoClient
import sys
import datetime

def copy_users_to_dashboard():
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Get source database name from user input
        source_db_name = input("Enter the name of your current database: ")
        source_db = client[source_db_name]
        
        # Create destination database
        dest_db = client['Dashboard']
        
        # Check if users collection exists in source database
        if 'users' not in source_db.list_collection_names():
            print(f"Error: 'users' collection not found in {source_db_name} database.")
            return False
        
        # Get count of documents to copy
        doc_count = source_db.users.count_documents({})
        print(f"Found {doc_count} user documents to copy.")
        
        # Check if users collection already exists in destination
        if 'users' in dest_db.list_collection_names():
            print("'users' collection already exists in Dashboard database.")
            # Create a new collection with timestamp instead of overwriting
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            new_collection_name = f"users_{timestamp}"
            print(f"Creating new collection: {new_collection_name}")
            
            # Copy all documents from source to the new collection
            docs = list(source_db.users.find())
            if docs:
                result = dest_db[new_collection_name].insert_many(docs)
                print(f"Successfully copied {len(result.inserted_ids)} user documents to {new_collection_name} collection.")
            else:
                print("No documents found to copy.")
            
            # Create indexes if they exist in the source collection
            for index in source_db.users.list_indexes():
                # Skip the _id_ index as it's created automatically
                if index['name'] != '_id_':
                    keys = index['key'].items()
                    dest_db[new_collection_name].create_index(keys)
                    print(f"Created index: {index['name']}")
        else:
            # If users collection doesn't exist, create it
            docs = list(source_db.users.find())
            if docs:
                result = dest_db.users.insert_many(docs)
                print(f"Successfully copied {len(result.inserted_ids)} user documents to users collection.")
            else:
                print("No documents found to copy.")
            
            # Create indexes if they exist in the source collection
            for index in source_db.users.list_indexes():
                # Skip the _id_ index as it's created automatically
                if index['name'] != '_id_':
                    keys = index['key'].items()
                    dest_db.users.create_index(keys)
                    print(f"Created index: {index['name']}")
        
        # List all collections in the Dashboard database
        collections = dest_db.list_collection_names()
        print(f"\nCollections in Dashboard database: {', '.join(collections)}")
        
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False
    finally:
        # Close the connection
        client.close()
        print("MongoDB connection closed.")

if __name__ == "__main__":
    print("Database Migration Tool: Copy Users to Dashboard Database")
    print("-------------------------------------------------------")
    
    success = copy_users_to_dashboard()
    
    if success:
        print("\nMigration completed successfully!")
    else:
        print("\nMigration failed or was cancelled.")
    
    input("\nPress Enter to exit...")