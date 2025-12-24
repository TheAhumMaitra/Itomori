
export default function Page() {
  return (
    <div className="min-h-screen m-3">
      <div className=" sm:min-w-full border-b-4 pb-3 flex flex-col justify-between items-center">
        <div className="mt-7">
          <h1>About Itomori</h1>
        </div>
      </div>
      <div className="text-center mt-10 w-85 h-full sm:w-full text-wrap border-background shadow-2xl shadow-primary bg-card p-3 rounded-2xl font-bold border-4">
        <p className="w-full">
          Itomori is a blazingly fast, easy to use quick note taking TUI app. It stores notes using json format.
        </p>
      </div>
    </div>
  );
}
