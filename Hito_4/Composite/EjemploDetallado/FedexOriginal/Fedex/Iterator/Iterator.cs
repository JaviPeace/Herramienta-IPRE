namespace Fedex;

public interface Iterator
{
    Component GetNext();
    bool HasMore();

}