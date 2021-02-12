import React, { useState } from 'react';
import {
  Step1,
  Step2,
  Step3,
  Step4,
} from './steps';

const MainForm = () => {
  const [page, setPage] = useState(1);
  const [form, setForm] = useState({});
  const [isPosting, setIsPosting] = useState(false);

  const nextPage = (data) => {
    setForm({ ...form, ...data });
    setPage(page + 1);
  }

  const sendData = (e) => { // simulate network
    e.preventDefault();
    setIsPosting(true);
    setTimeout(() => {
      setIsPosting(false);
      setTimeout(() => {
        setPage(4);
      }, 100);
    }, 1500);
  }

  switch (page) {
    case 1:
      return <Step1 onSubmit={nextPage} />;
    case 2:
      return <Step2 onSubmit={nextPage} />;
    case 3:
      return <Step3 form={form} onSubmit={sendData} isPosting={isPosting} />;
    case 4:
      return <Step4 />;
    default:
      return (
        <div>
          <h1>Unknown page</h1>
          <p>Very sneaky</p>
        </div>
      );
  }
}

export default MainForm;
