export interface IPricingCard {
  label?: string;
  badge?: string;
  plan: string;
  plan_price: string | number;
  old_price?: string;
  plan_term: string;
  discount_note?: string;
  subtitle: string;
  features: string[];
  button ?: string;
}