import * as v from "valibot";

export const schema = v.object({
  name: v.pipe(
    v.string(),
    v.minLength(1, "Ism kiritilishi shart"),
    v.minLength(2, "Ism juda qisqa"),
    v.maxLength(50, "Ism juda uzun"),
  ),
  email: v.pipe(
    v.string(),
    v.minLength(1, "Email kiritilishi shart"),
    v.email("Email formati noto'g'ri"),
    v.maxLength(75, "email juda uzun"),
  ),
  subject: v.pipe(
    v.string(),
    v.minLength(1, "Mavzu kiritilishi shart"),
    v.maxLength(100, "mavzu juda uzun"),
  ),
  message: v.pipe(
    v.string(),
    v.minLength(1, "Xabar kiritilishi shart"),
    v.minLength(10, "Xabar juda qisqa, kamida 10 belgi"),
    v.maxLength(300, "xabar juda uzun , 300 tadan oshmasin"),
  ),
});

export type Schema = v.InferOutput<typeof schema>;
