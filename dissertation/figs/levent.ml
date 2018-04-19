type lambda =
  (* ... *)
  | Levent of lambda * lambda_event
  (* ... *)

type lambda_event = {
  lev_loc : Location.t;
  lev_kind : lambda_event_kind;
  lev_repr : int Pervasives.ref option;
  lev_env : Env.summary;
}

type lambda_event_kind =
  | Lev_before
  | Lev_after of Types.type_expr
  | Lev_function
  | Lev_pseudo