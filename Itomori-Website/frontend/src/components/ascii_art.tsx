export default function ASCIILogo() {
  return (
    <div className="bg-muted/50 rounded-3xl border-chart-4 p-3 border-4 m-4">
      <pre className="text-2xl text-center font-bold text-chart-4">
        {String.raw`
.___  __                              .__
|   |/  |_  ____   _____   ___________|__|
|   \   __\/  _ \ /     \ /  _ \_  __ \  |
|   ||  | (  <_> )  Y Y  (  <_> )  | \/  |
|___||__|  \____/|__|_|  /\____/|__|  |__|
`}
      </pre>
    </div>
  );
}
