from collections import deque

class EventProcessingSystem:
    def __init__(self):
        self.event_queue = deque()

    def add_event(self, event):
        """Add a new event to the queue"""
        self.event_queue.append(event)
        print(f"Event '{event}' added to queue.")

    def process_next_event(self):
        """Process and remove the oldest event"""
        if self.event_queue:
            event = self.event_queue.popleft()
            print(f"Processing event: {event}")
        else:
            print("No events to process.")

    def display_pending_events(self):
        """Display all events currently in queue"""
        if self.event_queue:
            print("Pending Events:", list(self.event_queue))
        else:
            print("No pending events.")

    def cancel_event(self, event):
        """Cancel a specific event if not yet processed"""
        if event in self.event_queue:
            self.event_queue.remove(event)
            print(f"Event '{event}' canceled.")
        else:
            print(f"Event '{event}' not found or already processed.")


# Example Usage
if __name__ == "__main__":
    system = EventProcessingSystem()
    system.add_event("Login Request")
    system.add_event("File Upload")
    system.add_event("Database Backup")

    system.display_pending_events()

    system.cancel_event("File Upload")
    system.display_pending_events()

    system.process_next_event()
    system.display_pending_events()
