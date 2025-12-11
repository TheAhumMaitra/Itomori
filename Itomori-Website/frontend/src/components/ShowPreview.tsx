//  SPDX-FileCopyrightText: 2025-present Ahum Maitra theahummaitra@gmail.com

//  SPDX-License-Identifier: 	GPL-3.0-or-later


export default function ShowPreview() {
  return (
    <>
      <div className="w-full flex justify-center border-border border-4 items-center mt-4 flex-col gap-3 h-[90vh]">
        <h1 className="font-extrabold text-3xl mb-3 underline font-sans">
         Preview of Itomori:
        </h1>
        <video width="900" height="400" controls autoPlay loop muted>
          <source src="/Show_off.mp4" type="video/mp4" />
          Sorry, I tried but your browser does not support the video tag. It's too old!
        </video>
      </div>
    </>
  );
}
