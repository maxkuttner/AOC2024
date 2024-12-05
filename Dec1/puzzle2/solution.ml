(* Read data from a file *)
let read_data file_name =
  let ic = open_in file_name in
  let rec loop acc =
    try
      let line = input_line ic in
      let nums = List.map int_of_string (String.split_on_char ' ' (String.trim line)) in
      match nums with
      | [x; y] -> loop ((x, y) :: acc)
      | _ -> failwith "Malformed line in file"
    with End_of_file ->
      close_in ic;
      List.rev acc
  in
  loop []

(* Main program *)
let () =
  let data = read_data "Dec1/puzzle2/data.txt" in
  let n = List.length data in

  (* Tipp: fst gives first element and snd the second *)
  let l1 = List.map fst data in
  let l2 = List.map snd data in
  
  (* similiar to python solution keep track of count through a has table *)
  let count = Hashtbl.create n in
  List.iter (fun y ->
    Hashtbl.replace count y ((Hashtbl.find_opt count y |> Option.value ~default:0) + 1)
  ) l2;

  (* Compute the score *)
  let score =
    List.fold_left (fun acc x ->
      acc + x * (Hashtbl.find_opt count x |> Option.value ~default:0)
    ) 0 l1
  in

  Printf.printf "%d\n" score