import java.math.BigDecimal;

public class Expense {
      
    private int id;
    private static int nextId;
    private String title;
    private String description;
    private BigDecimal amount;
    private ExpenseCategory category;


    public Expense (int id, String title, String description, BigDecimal amount, ExpenseCategory category){
        this.id = nextId++;
        this.title = title;
        this.description = description;
        this.amount = amount;
        this.category = category;
}
    //getters

    public int getId(){
        return id;
    }

    public String getTitle(){
        return title;
    }

    public String getDescription(){
        return description;
    }

    public BigDecimal getAmount(){
        return amount;
    }

    public ExpenseCategory getCategory(){
        return category;
    }

    //setters 

        public void setDescription(String description) {

        this.description = description;

    }

    public void setAmount(BigDecimal amount) {

        this.amount = amount;

    }

    public void setCategory(ExpenseCategory category) {

        this.category = category;

    }

    @Override 
    public String toString(){
        return "Expense ID: " + id

            + "\nTitle: " + title

            + "\nDescription: " + description

            + "\nAmount: ₦" + amount.toPlainString()

            + "\nCategory: " + category;
    }
}
