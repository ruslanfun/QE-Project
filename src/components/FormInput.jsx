import React from 'react';

const errorMessage = (error) => {
  if (error.message) {
    return error.message;
  }
  switch (error.type) {
    case 'required':
      return 'Required field';
    default:
      return 'Invalid value';
  }
}

const FormInput = React.forwardRef(({ id, label, errors, type = 'text' }, ref) => {
  console.log(errors);
  return (
    <div className='mb-3'>
      <label htmlFor={id} className='form-label'>{label}</label>
      <input type={type} className={errors[id] ? 'form-control is-invalid' : 'form-control'} id={id} name={id} ref={ref} />
      {errors[id] && <div className='invalid-feedback'>{errorMessage(errors[id])}</div>}
    </div>
  );
});

export default FormInput;
