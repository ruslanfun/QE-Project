import React from 'react';
import { useForm } from 'react-hook-form';
import FormInput from '../FormInput';

const Step1 = ({ onSubmit }) => {
  const { register, handleSubmit, errors } = useForm();

  return (
    <div>
      <form onSubmit={handleSubmit(onSubmit)}>
        <h1>Step 1</h1>

        <FormInput id='email' label='Email' type='email' ref={register({ required: true, pattern: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,}$/ })} errors={errors} />

        <FormInput id='password' label='Password' type='password' ref={register({ required: true })} errors={errors} />

        <button type='submit' className='btn btn-primary'>Next</button>

      </form>
    </div>
  );
}

export default Step1;
