# Discount Calculator

A flexible, strategy-pattern-based discount engine that calculates the best price for a product given a user's tier and a set of discount rules.

## Usage

Run the script directly:

```bash
python discount_calculator.py
```

The main block at the bottom of the file demonstrates the engine with a sample product and user tier.

### Example output

```
Best price for Wireless Mouse for Premium user: $40.00
```

## Architecture

The system uses the **Strategy Pattern** via an abstract base class (`DiscountStrategy`) to make discount rules interchangeable and independently testable.

### Classes

**`Product`** — A simple data container holding a product's `name` and `price`.

**`DiscountStrategy` (abstract)** — Defines the interface all discount strategies must implement: `is_applicable()` to check eligibility, and `apply_discount()` to compute the discounted price.

**`PercentageDiscount`** — Applies a percentage-based reduction. Applicable only when the discount is 70% or less.

**`FixedAmountDiscount`** — Subtracts a fixed amount. Applicable only when the discounted price remains above 90% of the original price.

**`PremiumUserDiscount`** — Applies a 20% flat discount. Applicable only for users with the `premium` tier.

**`DiscountEngine`** — Accepts a list of strategies and runs all applicable ones against a product. Returns the lowest resulting price.

## Discount rules

| Strategy | Condition | Discount |
|---|---|---|
| `PercentageDiscount(n)` | `n <= 70` | `n%` off |
| `FixedAmountDiscount(n)` | `price × 0.9 > n` | Flat `$n` off |
| `PremiumUserDiscount` | User tier is `"premium"` | 20% off |

The engine always returns the **best (lowest) price** across all applicable strategies.


