namespace Fedex;

public class BFSIteratorWithoutBoxes : Iterator
{
    private Queue<Component> queue = new Queue<Component>();

    public BFSIteratorWithoutBoxes(Component root)
        => queue.Enqueue(root);
    

    
    public Component GetNext()
    {
        while (queue.Count > 0)
        {
            Component node = queue.Dequeue();
            foreach (Component child in node.GetChildren())
            {
       
                queue.Enqueue(child);
                
            }
            
            if (node is Item)
            {
                return node;
            }
        }

        return null; 
    }

    public bool HasMore()
        => queue.Any(); 
}