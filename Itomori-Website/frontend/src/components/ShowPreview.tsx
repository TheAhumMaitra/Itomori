export default function ShowPreview() {
  return (
    <>
      <div className="w-full flex justify-center border-border border-4 items-center mt-4 flex-col gap-3 h-[80vh]">
        <h1 className="font-extrabold text-3xl underline font-sans">
          A brief introduction video:
        </h1>
        <video width="900" height="400" controls preload="none">
          <source src="public/Show_off.mp4" type="video/mp4" />
          Sorry, I tried but your browser does not support the video tag. It's too old!
        </video>
      </div>
    </>
  );
}
