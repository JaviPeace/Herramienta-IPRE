namespace Fedex;

public class BFSIterator:Iterator
{
    /*
     * Un "Queue" es una lista con dos operaciones.
     *  - Enqueue(Component n) -> agrega "n" al final de la lista. Algo así como un "append(n)" en python.
     *  - Dequeue()            -> saca el primer elemento de la lista y lo retorna. Algo así como un "pop(0)" en python.
     */
    private Queue<Component> queue = new Queue<Component>();

    public BFSIterator(Component root)
        => queue.Enqueue(root);
    
    public Component GetNext()
    {
        Component node = queue.Dequeue();
        foreach (Component child in node.GetChildren())
            queue.Enqueue(child);
        
        return node;
    }

    public bool HasMore()
        => queue.Any(); // verdadero solo si no quedan elementos en el queue
}